from django.test import TestCase
from .forms import CommentForm, SearchForm, PostCreateForm


class CommentFormTest(TestCase):
    def test_valid_comment_form(self):
        form_data = {'body': 'This is a valid comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class SearchFormTest(TestCase):
    def test_valid_search_form(self):
        form_data = {'search': 'Search query'}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        form_data = {'search': ''}
        form = SearchForm(data=form_data)
        self.assertFalse(form.is_valid())
