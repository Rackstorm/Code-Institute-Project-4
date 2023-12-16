from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

# Choices for the status field in the Post model
STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    """
    Model representing a category for posts.

    Attributes:
        title (str): The title of the category.
    """
    title = models.CharField(max_length=200, unique=True, verbose_name="Category")

    def __str__(self):
        return self.title

class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post.
        slug (AutoSlugField): The slug for the post.
        author (User): The author of the post.
        category (Category): The category to which the post belongs.
        featured_image (CloudinaryField): The featured image for the post.
        excerpt (str): A brief excerpt of the post.
        updated_on (DateTimeField): The last update timestamp.
        content (str): The content of the post.
        created_on (DateTimeField): The creation timestamp.
        status (int): The status of the post (Draft or Published).
        likes (ManyToManyField): Users who liked the post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def delete_post(self):
        self.delete()

class PostLike(models.Model):
    """
    Model representing a like for a specific post by a user.

    Attributes:
        post (Post): The post that is liked.
        user (User): The user who liked the post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (Post): The post to which the comment belongs.
        name (str): The name of the commenter.
        email (EmailField): The email of the commenter.
        body (str): The content of the comment.
        created_on (DateTimeField): The creation timestamp.
        approved (bool): Indicates whether the comment is approved or not.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (User): The user to whom the profile belongs.
        bio (str): A biography or description of the user.
        profile_picture (CloudinaryField): The profile picture of the user.
        liked_posts (ManyToManyField): Posts liked by the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    liked_posts = models.ManyToManyField(Post, related_name='liked_by', blank=True)

    def __str__(self):
        return self.user.username
