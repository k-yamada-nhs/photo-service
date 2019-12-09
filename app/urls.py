from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    # トップ
    path('', views.index, name='index'),
    # マイページ
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    # タイムライン
    path('users/timeline', views.users_timeline, name='users_timeline'),
    # プロジェクト作成
    path('projects/create/', views.projects_create, name='projects_create'),
    # プロジェクト詳細
    path('projects/<int:pk>/', views.projects_detail, name='projects_detail'),
    # プロジェクト更新
    path('projects/<int:pk>/update', views.projects_update, name='projects_update'),
    # プロジェクト削除
    path('projects/<int:pk>/delete', views.projects_delete, name='projects_delete'),
    # スタイル変換
    path('test_ajax', views.test_ajax, name='test_ajax'),
    # コメント
    path('comment_ajax/<int:pk>', views.comment_ajax, name='comment_ajax'),
    # いいね
    path('like/<int:pk>', views.like, name='like'),
    # リアルタイム変換
    path('realtime_transfer', views.realtime_transfer, name='realtime_transfer'),
]
