from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class SignUpForm(UserCreationForm):
    
    profile_image = forms.ImageField()

    class Meta:
        mdoel = User
        fields = ("username", "password1", "password2", "profile_image")