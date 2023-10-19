from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_item_name_is_required(self):
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        expected_fields = ['name', 'message', 'email']
        actual_fields = form.Meta.fields
        self.assertEqual(set(expected_fields), set(actual_fields))
