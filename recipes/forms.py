from django import forms
from allauth.account.forms import SignupForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Comment, Post, Category, Profile


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
            'content': SummernoteWidget(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }



class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    profile_picture = forms.ImageField(required=False)

    def save(self, request, user):
        user.profile.bio = self.cleaned_data.get('bio', '')
        user.profile.profile_picture = self.cleaned_data.get('profile_picture', None)
        user.profile.save()
        return user

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']