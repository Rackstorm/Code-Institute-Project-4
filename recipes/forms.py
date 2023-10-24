from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
    search.widget.attrs.update({'class': 'form-control'})
    search.widget.attrs.update({'placeholder': 'Search for a recipe'})


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'excerpt', 'content', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}), }
