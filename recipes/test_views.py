from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class PostListViewTest(TestCase):
    def test_post_list_view(self):
        # Test if the post list view returns a status code 200 and uses the correct template.
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', slug='test-post', author=self.user, content='Test content', status=1)

    def test_post_detail_view(self):
        # Test if the post detail view for a valid post slug returns a status code 200 and uses the correct template.
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_detail_view_with_invalid_slug(self):
        # Test if the post detail view for an invalid post slug returns a status code 404.
        response = self.client.get(reverse('post_detail', args=['invalid-slug']))
        self.assertEqual(response.status_code, 404)


class PostlikeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', slug='test-post', author=self.user, content='Test content', status=1)
        self.client.login(username='testuser', password='testpassword')

    def test_post_like_view(self):
        # Test if the post like view for a valid post slug returns a status code 302 (redirect) and correctly updates the likes count and the user who liked the post.
        response = self.client.post(reverse('post_like', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        updated_post = Post.objects.get(slug=self.post.slug)
        self.assertEqual(updated_post.likes.count(), 1)
        self.assertEqual(updated_post.likes.first().username, 'testuser')
