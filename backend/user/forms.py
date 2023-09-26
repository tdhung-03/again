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
        'id': "formInput#text",
        'type': 'text',
        'name': "text",
        'placeholder': 'e.g. Duy',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#text",
        'type': 'text',
        'name': "text",
        'placeholder': 'e.g. Hung',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'id': "formInput#text",
        'type': 'text',
        'name': "text",
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
        'id': "formInput#passowrd",
        'type': "password",
        'name': "password",
        'placeholder': "••••••••",
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': "input input--password",
        'id': "formInput#confirm-passowrd",
        'type': "password",
        'name': "confirm-password",
        'placeholder': "••••••••",
    }))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'short_intro', 'bio', 'location', 'social_github',
                  'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']
