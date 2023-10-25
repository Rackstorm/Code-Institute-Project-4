from django.test import TestCase
from .forms import CommentForm, SearchForm, PostCreateForm


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
