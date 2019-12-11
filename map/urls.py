from django.conf.urls import url
from . import views
app_name = "map"
urlpatterns = [
    url('', views.locationmap, name='locationmap'),
]