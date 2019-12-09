from django.contrib.auth.models import User
from django.conf import settings

from app.models import Photo, Relationship
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def locationmap(request):
    return render(request, 'map/locationmap.html')

def ajax_projectdata(request):
    projects_to_json = serializers.serialize("json", Photo.objects.all())
    
    d = {
        # 'projects': projects_to_json,
        'projects': "a",
    }

    return JsonResponse(d)