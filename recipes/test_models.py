""" Test cases for the models of the recipes app. """
import os

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Category, Comment, Post, Profile


class CategoryModelTest(TestCase):
    """ Test case for the Category model. """

    def test_category_creation(self):
        """ Test if a category is created correctly with the expected attributes. """
        category = Category.objects.create(title="Test Category")
        self.assertEqual(str(category), "Test Category")


class PostModelTest(TestCase):
    """ Test case for the Post model. """

    def setUp(self):
        user = User.objects.create_user('testuser', password='testpassword')
        category = Category.objects.create(title="Test Category")
        image_path = os.path.join(os.path.dirname(
            __file__), '../static/images/fresh-organic-vegetables-4.jpg')
        image = SimpleUploadedFile("test_image.jpg", content=open(
            image_path, 'rb').read(), content_type="image/jpeg")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=user,
            category=category,
            featured_image=image,
            excerpt="Test excerpt",
            content="Test content",
            status=1
        )

    def test_post_creation(self):
        """ Test if a post is created correctly with the expected attributes. """
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post.category), "Test Category")
        self.assertEqual(self.post.status, 1)

    def test_number_of_likes(self):
        """ Test if the number of likes for a post is correctly calculated. """
        user = User.objects.create_user('testuser2', password='testpassword')
        self.post.likes.add(user)
        self.assertEqual(self.post.number_of_likes(), 1)


class CommentModelTest(TestCase):
    """ Test case for the Comment model. """

    def setUp(self):
        user = User.objects.create_user('testuser', password='testpassword')
        category = Category.objects.create(title="Test Category")
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=user,
            category=category,
            excerpt="Test excerpt",
            content="Test content",
            status=1
        )
        self.comment = Comment.objects.create(
            post=post,
            name="Test User",
            email="test@example.com",
            body="Test comment"
        )

    def test_comment_creation(self):
        """  Test if a comment is created correctly with the expected attributes. """
        self.assertEqual(self.comment.name, "Test User")
        self.assertEqual(self.comment.email, "test@example.com")
        self.assertEqual(self.comment.body, "Test comment")
        self.assertEqual(self.comment.approved, False)
        self.assertEqual(str(self.comment.post), "Test Post")


class ProfileModelTest(TestCase):
    """ Test case for the Profile model. """

    def setUp(self):
        user = User.objects.create_user('testuser', password='testpassword')
        self.profile = Profile.objects.create(
            user=user,
            bio="Test bio",
            profile_picture=SimpleUploadedFile(
                "test_image.jpg",
                content=open(
                    os.path.join(os.path.dirname(
                        __file__), '../static/images/fresh-organic-vegetables-4.jpg'),
                    'rb'
                ).read(),
                content_type="image/jpeg"
            )
        )

    def test_profile_creation(self):
        """ Test if a profile is created correctly with the expected attributes. """
        self.assertEqual(str(self.profile.user.profile), "Test User's Profile")
        self.assertEqual(self.profile.bio, "Test bio")
        self.assertIsNotNone(self.profile.profile_picture)

    def test_profile_str_representation(self):
        """ Test if the string representation of a profile is as expected. """
        self.assertEqual(str(self.profile), "Test User's Profile")
