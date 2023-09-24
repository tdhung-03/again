from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','last_name','email','username','password1','password2']

        