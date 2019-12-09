from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.conf import settings
import os
from .models import Photo, Relationship, Comnt, Reply, Like
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm, CmntForm
from django.contrib import messages
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import time
from django.contrib import messages
from app.modules.faststyle import styletransfer
from django.views import generic
from django.db.models import Q

# トップ
def index(request):
    return render(request, 'app/index.html')

# プロジェクト作成
@login_required
def projects_create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, "投稿が完了しました")
            return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'app/projects_create.html', {'form': form})

# プロジェクト詳細
def projects_detail(request, pk):
    project = get_object_or_404(Photo, pk=pk)
    comnt = Comnt.objects.filter(target=project)
    like = Like.objects.filter(post=project)
    commentform = CmntForm()

    return render(request, 'app/projects_detail.html', {'project': project, 'commentform': commentform, 'cmnt': comnt, 'like': like })

# プロジェクト削除
@require_POST
def projects_delete(request, pk):
    project = get_object_or_404(Photo, pk=pk)
    project.delete()
    return redirect('app:users_detail', request.user_id)

# プロジェクト更新
def projects_update(request, pk):

    return render(request, 'app/projects_update.html')

# ユーザー詳細
def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    projects = user.photo_set.all().order_by('-created_at')

    # フォローとフォロワーを取得
    follows = Relationship.objects.filter(follow=user.id)
    followers = Relationship.objects.filter(follower=user.id)

    return render(request, 'app/users_detail.html', {'user': user, 'projects': projects, 'follows': follows, 'followers': followers})

# タイムライン兼検索
@login_required
def users_timeline(request):
    
    # 検索キーワード受け取り
    keyword = request.GET.get("title")

    if keyword:

        # キーワード検索
        projects = Photo.objects.filter(title__icontains=keyword)
    else:
        
        # 自分の作品とフォローしてる人の作品
        projects = Photo.objects.filter(Q(user=request.user) | Q(user=request.user))
    
    return render(request, 'app/users_timeline.html', {'projects': projects})

# スタイル変換
def test_ajax(request):

    base = request.GET.get('base')
    style = request.GET.get('style')
   
    path = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")

    # pathの生成
    output_path = path + "/static/images/out/" + timestr + ".jpg"
    input_path = path + base
    model_path = "model/"+ style +".ckpt"

    # style transfer
    styletransfer.ffwd_to_img(input_path, output_path, model_path)

    # 画像の保存先のpath
    hoge = {
        "base": base,
        "style": style,
        "out": "/static/images/out/" + timestr + ".jpg",
        "msg": "send-ok"
    }
    
    return JsonResponse(hoge)

# リアルタイムスタイル変換
def realtime_transfer(request):
    return render(request, 'app/realtime_transfer.html')

# コメント用
def comment_ajax(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    form = CmntForm(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.user = request.user
        comment.save()
        return redirect('app:projects_detail', pk=pk)

# いいね
def like(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    is_like = Like.objects.filter(user=request.user).filter(post=post).count()
    # いいね済み
    if is_like > 0:
        # 削除
        messages.warning(request, "いいね済みです")
        return redirect('app:projects_detail', pk=pk)

    # いいねしてない
    like = Like()
    like.user = request.user
    like.post = post
    like.save()
    messages.success(request, "いいねしました")
    return redirect('app:projects_detail', pk=pk)




