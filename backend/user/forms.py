from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#first_name",
        'type': 'text',
        'name': "first_name",
        'placeholder': 'e.g. Duy',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#last_name",
        'type': 'text',
        'name': "last_name",
        'placeholder': 'e.g. Hung',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#username",
        'type': 'text',
        'name': "username",
        'placeholder': 'e.g. tdhung03',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input input--email',
        'id': "formInput#email",
        'type': 'email',
        'name': "email",
        'placeholder': 'e.g. user@domain.com',
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': "input input--password",
        'id': "formInput#password",
        'type': "password",
        'name': "password",
        'placeholder': "••••••••",
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': "input input--password",
        'id': "formInput#confirm-password",
        'type': "password",
        'name': "confirm-password",
        'placeholder': "••••••••",
    }))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'short_intro', 'bio', 'location', 'social_github',
                  'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']

    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#name",
        'type': 'text',
        'name': "name",
        'placeholder': 'e.g. Duy Hung',
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#username",
        'type': 'text',
        'name': "username",
        'placeholder': 'e.g. tdhung03',
    }))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'id': "formInput#email",
        'type': 'text',
        'name': "email",
        'placeholder': 'e.g. user@gmail.com',
    }))
    short_intro = forms.CharField(label='Intro', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#intro",
        'type': 'text',
        'name': "intro",
    }))
    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#bio",
        'type': 'text',
        'name': "bio",
    }))
    location = forms.CharField(label='Location', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#location",
        'type': 'text',
        'name': "location",
        'placeholder': 'e.g. US',
    }))
    social_github = forms.CharField(label='GitHub', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#github",
        'type': 'text',
        'name': "github",
    }))
    social_twitter = forms.CharField(label='Twitter', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#twitter",
        'type': 'text',
        'name': "twitter",
    }))
    social_linkedin = forms.CharField(label='LinkedIn', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#linkedin",
        'type': 'text',
        'name': "linkedin",
    }))
    social_youtube = forms.CharField(label='Youtube', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#youtube",
        'type': 'text',
        'name': "youtube",
    }))
    social_website = forms.CharField(label='Website', widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#website",
        'type': 'text',
        'name': "website",
    }))
