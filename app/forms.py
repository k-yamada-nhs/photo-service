from django.forms import ModelForm
from .models import Photo, UploadImage
from django import forms

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'comment', 'baseimagepath', 'styleimagepath', 'outputimagepath']
        widgets = {
            'baseimagepath': forms.HiddenInput,
            'styleimagepath': forms.HiddenInput,
            'outputimagepath': forms.HiddenInput,
        }