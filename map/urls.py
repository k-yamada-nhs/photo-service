from django.conf.urls import url
from . import views
app_name = "map"
urlpatterns = [
    url('', views.locationmap, name='locationmap'),
    url('ajax_projectdata', views.ajax_projectdata, name='ajax_projectdata')
]