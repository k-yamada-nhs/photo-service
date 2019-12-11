from django.forms import ModelForm
from .models import Photo, Comnt
from django import forms

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'comment', 'baseimagepath', 'styleimagepath', 'outputimagepath', 'latitude', 'longitude']
        widgets = {
            'baseimagepath': forms.HiddenInput,
            'styleimagepath': forms.HiddenInput,
            'outputimagepath': forms.HiddenInput,
        }
 
class CmntForm(ModelForm):
    class Meta:
        model = Comnt
        fields = ['text']