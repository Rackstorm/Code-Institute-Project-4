from django.test import TestCase
from .forms import CommentForm, SearchForm, PostCreateForm, CustomSignupForm, ProfileEditForm
from django.core.files.uploadedfile import SimpleUploadedFile

class CommentFormTest(TestCase):
    # Testing the validity when provided with a valid "body" field and assert that the form is valid.
    def test_valid_comment_form(self):
        form_data = {'body': 'This is a valid comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Testing the validity when provided with an invalid "body" field and assert that the form is invalid.
    def test_invalid_comment_form(self):
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Add more tests as needed for CommentForm...

class SearchFormTest(TestCase):
    # Testing the validity when provided with a valid "search" field and assert that the form is valid.
    def test_valid_search_form(self):
        form_data = {'search': 'Search query'}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Testing the validity when provided with an invalid "search" field and assert that the form is invalid.
    def test_invalid_search_form(self):
        form_data = {'search': ''}
        form = SearchForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Add more tests as needed for SearchForm...

class PostCreateFormTest(TestCase):
    # Testing the validity when provided with valid data and assert that the form is valid.
    def test_valid_post_create_form(self):
        form_data = {
            'title': 'Test Title',
            'excerpt': 'Test Excerpt',
            'content': 'Test Content',
            'category': 1,
            'status': 'published'
        }
        form = PostCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Testing the validity when provided with invalid data and assert that the form is invalid.
    def test_invalid_post_create_form(self):
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
    # Testing the validity of the custom signup form
    def test_valid_custom_signup_form(self):
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

    # Testing the validity when provided with invalid data and assert that the form is invalid.
    def test_invalid_custom_signup_form(self):
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
    # Testing the validity when provided with valid data and assert that the form is valid.
    def test_valid_profile_edit_form(self):
        form_data = {
            'bio': 'Updated test bio.',
            'profile_picture': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = ProfileEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Testing the validity when provided with invalid data and assert that the form is invalid.
    def test_invalid_profile_edit_form(self):
        form_data = {
            'bio': '', 
            'profile_picture': 'invalid_file', 
        }
        form = ProfileEditForm(data=form_data)
        self.assertFalse(form.is_valid())

