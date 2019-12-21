from django.urls import path
from . import views
app_name = 'map'
urlpatterns = [
    path('location/<int:pk>', views.locationmap, name='locationmap'),
]