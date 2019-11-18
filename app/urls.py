from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    path('users/timeline', views.users_timeline, name='users_timeline'),
    path('projects/create/', views.projects_create, name='projects_create'),
    path('projects/<int:pk>/', views.projects_detail, name='projects_detail'),
    path('projects/<int:pk>/delete', views.projects_delete, name='projects_delete'),
    path('test_ajax', views.test_ajax, name='test_ajax'),
    path('ajax_post_search', views.ajax_post_search, name='ajax_post_search'),
    path('realtime_transfer', views.realtime_transfer, name='realtime_transfer'),
]
