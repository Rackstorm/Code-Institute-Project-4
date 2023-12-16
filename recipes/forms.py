from django import forms
from allauth.account.forms import SignupForm
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post, Category, Profile


# Form for adding comments to a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for searching recipes
class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
    search.widget.attrs.update({'class': 'form-control'})
    search.widget.attrs.update({'placeholder': 'Search for a recipe'})


# Form for creating a new post
class PostCreateForm(forms.ModelForm):
    class Meta:
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


# Custom signup form extending Allauth's SignupForm
class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    profile_picture = forms.ImageField(required=False)

    # Custom save method to update the user profile
    def save(self, request, user):
        user.profile.bio = self.cleaned_data.get('bio', '')
        user.profile.profile_picture = self.cleaned_data.get('profile_picture', None)
        user.profile.save()
        return user


# Form for editing a user's profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
