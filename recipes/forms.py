from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
    search.widget.attrs.update({'class': 'form-control'})
    search.widget.attrs.update({'placeholder': 'Search for a recipe'})
