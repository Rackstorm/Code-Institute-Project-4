from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from .forms import CommentForm, SearchForm, PostCreateForm, CustomSignupForm, ProfileEditForm
from allauth.account.views import SignupView
from django.db.models import Q

# Custom SignupView that uses your CustomSignupForm
class CustomSignupView(SignupView):
    form_class = CustomSignupForm

# Generic ListView for displaying a list of published posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# View for displaying post details, handling comments, and likes
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        # Retrieve the post based on the slug from the URL
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Retrieve approved comments and check if the user has liked the post
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        # Render the post detail page with relevant information
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
        # Similar to the get method, but handles the submission of comments
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        # Process the submitted comment
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        # Render the post detail page with updated information
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

# View for handling post likes
class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        # Toggle the like status for the current user on the specified post
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Redirect back to the post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# View for handling post searches
class PostSearch(View):
    def get(self, request, *args, **kwargs):
        # Display the search form and search results based on the user's input
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

# View for creating new posts (requires login)
@login_required
def PostCreateView(request):
    if request.method == 'POST':
        # Handle the form submission to create a new post
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        # Display the form for creating a new post
        form = PostCreateForm()

    return render(request, 'post_create.html', {'form': form})

# View for editing an existing post (requires login)
@login_required
def edit_post(request, slug):
    # Retrieve the post to be edited and handle the form submission for editing
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostCreateForm(instance=post)

    # Display the form for editing the post
    return render(request, 'edit_post.html', {'form': form, 'post': post})

# View for displaying user profile information
@login_required
def ProfileView(request):
    # Retrieve user profile information, including liked and authored posts
    user_profile = Profile.objects.get(user=request.user)
    liked_posts = user_profile.liked_posts.all()
    user_posts = request.user.recipe_posts.all()
    
    # Render the user profile page with relevant information
    return render(request, 'profile.html', {'user_profile': user_profile, 'liked_posts': liked_posts, 'user_posts': user_posts})

# View for editing user profile information
@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Handle the form submission for editing user profile information
        form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # Display the form for editing user profile information
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

# View for deleting a post (requires login)
@login_required
def delete_post(request, slug):
    # Retrieve the post to be deleted and handle the form submission for deletion
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == 'POST':
        post.delete_post()
        return redirect('home')
    
    # Display the confirmation page for deleting the post
    return render(request, 'delete_post.html', {'post': post})
