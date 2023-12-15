from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from .forms import CommentForm, SearchForm, PostCreateForm, CustomSignupForm, ProfileEditForm
from allauth.account.views import SignupView
from django.db.models import Q

class CustomSignupView(SignupView):
    form_class = CustomSignupForm



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )



class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostSearch(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        results = []
        query = request.GET.get("q")
        if query:
            search_terms = query.split()
            search_query = Q()
            for term in search_terms:
                search_query |= Q(title__icontains=term, status=1)
                search_query |= Q(content__icontains=term, status=1)
            results = Post.objects.filter(search_query).distinct()
        return render(request, "post_search.html", {"form": form, "results": results})


@login_required
def PostCreateView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostCreateForm()

    return render(request, 'post_create.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostCreateForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def ProfileView(request):
    user_profile = Profile.objects.get(user=request.user)
    liked_posts = user_profile.liked_posts.all()
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})