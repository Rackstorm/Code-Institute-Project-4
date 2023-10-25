from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
import os


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(title="Test Category")
        self.assertEqual(str(category), "Test Category")


class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('testuser', password='testpassword')
        category = Category.objects.create(title="Test Category")
        image_path = os.path.join(os.path.dirname(__file__), '../static/images/fresh-organic-vegetables-4.jpg')
        image = SimpleUploadedFile("test_image.jpg", content=open(image_path, 'rb').read(), content_type="image/jpeg")
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
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post.category), "Test Category")
        self.assertEqual(self.post.status, 1)


class CommentModelTest(TestCase):
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
        self.assertEqual(self.comment.name, "Test User")
        self.assertEqual(self.comment.email, "test@example.com")
        self.assertEqual(self.comment.body, "Test comment")
        self.assertEqual(self.comment.approved, False)
        self.assertEqual(str(self.comment.post), "Test Post")
