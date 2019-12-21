from django.contrib.auth.models import User
from django.conf import settings

from app.models import Photo, Relationship
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def locationmap(request, pk):
    projects = Photo.objects.all()
    return render(request, 'map/locationmap.html', {'projects':  projects})
