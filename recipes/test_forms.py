""" Test cases for the forms in the recipes app. """
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import CommentForm, SearchForm, PostCreateForm, CustomSignupForm, ProfileEditForm


class CommentFormTest(TestCase):
    """ Test case for the CommentForm. """

    def test_valid_comment_form(self):
        """ Provided with a valid "body" field and assert that the form is valid. """
        form_data = {'body': 'This is a valid comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        """ Provided with an invalid "body" field and assert that the form is invalid. """
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class SearchFormTest(TestCase):
    """ Test case for the SearchForm."""

    def test_valid_search_form(self):
        """ Provided with a valid "search" field and assert that the form is valid. """
        form_data = {'search': 'Search query'}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        """ Provided with an invalid "search" field and assert that the form is invalid. """
        form_data = {'search': ''}
        form = SearchForm(data=form_data)
        self.assertFalse(form.is_valid())


class PostCreateFormTest(TestCase):
    """ Test case for the PostCreateForm. """

    def test_valid_post_create_form(self):
        """ Providing valid data and assert that the form is valid """
        form_data = {
            'title': 'Test Title',
            'excerpt': 'Test Excerpt',
            'content': 'Test Content',
            'category': 1,
            'status': 'published'
        }
        form = PostCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_post_create_form(self):
        """ Provided with invalid data and assert that the form is invalid. """
        form_data = {
            'title': '',
            'excerpt': '',
            'content': '',
            'category': '',
            'status': 'invalid_status'
        }
        form = PostCreateForm(data=form_data)
        self.assertFalse(form.is_valid())


class CustomSignupFormTest(TestCase):
    """ Test case for the CustomSignupForm. """

    def test_valid_custom_signup_form(self):
        """ Test the validity of the custom signup form. """
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'bio': 'This is a test bio.',
            'profile_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_custom_signup_form(self):
        """ Provided with invalid data and assert that the form is invalid. """
        form_data = {
            'username': 'testuser',
            'email': 'invalidemail',
            'password1': 'testpassword',
            'password2': 'differentpassword',
            'bio': 'This is a test bio.',
            'profile_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = CustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())


class ProfileEditFormTest(TestCase):
    """ Test case for the ProfileEditForm. """

    def test_valid_profile_edit_form(self):
        """
        Test the validity when provided with valid data and assert that the form is valid.
        """
        form_data = {
            'bio': 'Updated test bio.',
            'profile_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = ProfileEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_profile_edit_form(self):
        """ Provided with invalid data and assert that the form is invalid. """
        form_data = {
            'bio': '',
            'profile_picture': 'invalid_file',
        }
        form = ProfileEditForm(data=form_data)
        self.assertFalse(form.is_valid())
