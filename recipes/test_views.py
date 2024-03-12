""" Recipes app views unit tests module """
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post, Profile


class PostCreateViewTest(TestCase):
    """ Test case for the post create view. """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_post_create_view_get(self):
        """ Test if the post create view returns a status code 200 and uses the correct template. """
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')

    def test_post_create_view_post(self):
        """ Test if creating a post via post create view redirects and post is created. """
        response = self.client.post(reverse('post_create'), {
            'title': 'New Test Post',
            'featured_image': None,
            'excerpt': 'Test excerpt',
            'content': 'Test content',
            'category': None,
            'status': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.filter(
            title='New Test Post').exists(), True)


class ProfileViewTest(TestCase):
    """ Test case for the profile view. """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        """ Test if the profile view returns a status code 200 and uses the correct template. """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class EditProfileViewTest(TestCase):
    """ Test case for the edit profile view. """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_edit_profile_view_get(self):
        """ Test if the edit profile view returns a status code 200 and uses the correct template. """
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_edit_profile_view_post(self):
        """ Test if editing the profile via edit profile view returns code 302 and the profile is updated. """
        response = self.client.post(reverse('edit_profile'), {
            'bio': 'Updated bio',
            'profile_picture': None
        })
        self.assertEqual(response.status_code, 302)
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.bio, 'Updated bio')


class PostLikeViewTest(TestCase):
    """ Test case for the post like view. """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user, content='Test content', status=1)
        self.client.login(username='testuser', password='testpassword')

    def test_post_like_view(self):
        """ Test if the post like view for an invalid post slug returns a status code 404 (not found). """
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        updated_post = Post.objects.get(slug=self.post.slug)
        self.assertEqual(updated_post.likes.count(), 1)
        self.assertEqual(updated_post.likes.first().username, 'testuser')
