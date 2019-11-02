from django.forms import ModelForm
from .models import Photo, UploadImage
from django import forms

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'comment', 'image', 'category']
