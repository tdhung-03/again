from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'short_intro', 'bio', 'location', 'social_github',
                  'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']
