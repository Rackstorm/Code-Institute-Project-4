""" Importing necessary modules. """
from django import forms
from allauth.account.forms import SignupForm
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post, Profile

class CommentForm(forms.ModelForm):
    """ Form for adding comments to a post. """
    class Meta:
        """ Meta class for the CommentForm. """
        model = Comment
        fields = ('body',)

class SearchForm(forms.Form):
    """ Form for searching recipes."""
    search = forms.CharField(label='Search', max_length=100)
    search.widget.attrs.update({'class': 'form-control'})
    search.widget.attrs.update({'placeholder': 'Search for a recipe'})

class PostCreateForm(forms.ModelForm):
    """ Form for creating a new post. """
    class Meta:
        """ Meta class for the PostCreateForm. """
        model = Post
        fields = ['title', 'featured_image', 'excerpt', 'content', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomSignupForm(SignupForm):
    """ Custom signup form extending Allauth's SignupForm. """
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    profile_picture = forms.ImageField(required=False)

    def save(self, request):
        """ Custom save method to update the user profile. """
        user = super().save(request)
        user.profile.bio = self.cleaned_data.get('bio', '')
        user.profile.profile_picture = self.cleaned_data.get('profile_picture', None)
        user.profile.save()
        return user

class ProfileEditForm(forms.ModelForm):
    """ Form for editing a user's profile. """
    class Meta:
        """ Meta class for the ProfileEditForm. """
        model = Profile
        fields = ['bio', 'profile_picture']
