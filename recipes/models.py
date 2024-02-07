""" Implements the models for the recipes app. """
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """ Model representing a category for posts. """
    title = models.CharField(
        max_length=200, unique=True, verbose_name="Category")

    def __str__(self):
        return self.title


class Post(models.Model):
    """ Model with attributes for a blog post. """
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title',
                         unique=True, always_update=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    class Meta:
        """ Meta class for the Post model. """
        ordering = ["-created_on"]

    def __str__(self):
        """ Returns the title of a post. """
        return self.title

    def number_of_likes(self):
        """ Returns the number of likes for a post. """
        return self.likes.count()

    def delete_post(self):
        """ Deletes a post. """
        self.delete()


class PostLike(models.Model):
    """ Model representing a like for a specific post by a user. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    """ Model representing a comment on a blog post with attributes for the comment's author."""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Meta class for the Comment model. """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    """ Model representing a user profile with attributes for the user's bio and profile picture. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    liked_posts = models.ManyToManyField(
        Post, related_name='liked_posts', blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username
