""" This module contains the views for the recipes app. """
from allauth.account.views import SignupView
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Profile
from .forms import CommentForm, SearchForm, PostCreateForm, CustomSignupForm, ProfileEditForm


class CustomSignupView(SignupView):
    """ Custom SignupView that uses the CustomSignupForm. """
    form_class = CustomSignupForm

class PostList(generic.ListView):
    """ Generic ListView for displaying a list of published posts."""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetail(View):
    """ View for displaying post details, handling comments, and likes."""
    def get(self, request, slug, *args, **kwargs):
        """ Handles GET requests for post details."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Retrieve approved comments and check if the user has liked the post
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        # Render the post detail page with relevant informatio """
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "category": post.category,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Handles POST requests for submitting comments."""
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
                "category": post.category,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )

class PostLike(View):
    """ View for handling post likes. """
    def post(self, request, slug, *args, **kwargs):
        """ Toggle the like status for the current user on the specified post """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostSearch(View):
    """ View for handling post searches. """
    def get(self, request):
        """ Handles GET requests for displaying the search form and results."""
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
    """ View for creating new posts (requires login)."""
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
def edit_post(request, slug, *args, **kwargs):
    """ View for editing an existing post (requires login). """
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
    """ View for displaying user profile information. """
    user_profile = Profile.objects.get(user=request.user)
    liked_posts = user_profile.liked_posts.all()
    user_posts = request.user.recipe_posts.all()

    return render(request, 'profile.html', {'user_profile': user_profile, 'liked_posts': liked_posts, 'user_posts': user_posts})

@login_required
def edit_profile(request):
    """ View for editing user profile information."""
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_post(request, slug, *args, **kwargs):
    """ View for deleting a post (requires login)."""
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == 'POST':
        post.delete_post()
        return redirect('home')

    return render(request, 'delete_post.html', {'post': post})
