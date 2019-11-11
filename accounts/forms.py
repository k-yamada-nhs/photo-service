from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

#usercreateform
class UserCreateForm(UserCreationForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profileimage',]
