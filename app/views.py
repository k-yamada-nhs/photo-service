from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Photo, Relationship, UploadImage
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
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
        
    # 投稿用フォームと画像用フォーム
    return render(request, 'app/projects_create.html', {'form': form})


def projects_detail(request, pk):
    project = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/projects_detail.html', {'project': project})


@require_POST
def projects_delete(request, pk):
    project = get_object_or_404(Photo, pk=pk)
    project.delete()
    return redirect('app:users_detail', request.user_id)


def index(request):
    return render(request, 'app/index.html')

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    projects = user.photo_set.all().order_by('-created_at')

    # フォローとフォロワーを取得
    follows = Relationship.objects.filter(follow=user.id)
    followers = Relationship.objects.filter(follower=user.id)

    return render(request, 'app/users_detail.html', {'user': user, 'projects': projects, 'follows': follows, 'followers': followers})

# タイムライン
def users_timeline(request):
    user = request.user

    # 自分とフォローしているユーザーの投稿を取得
    projects = Photo.objects.all()

    return render(request, 'app/users_timeline.html', {'projects': projects, 'user': user})

@require_POST
def test_ajax(request):

    base = request.FILES['image']
    style = request.FILES['style']

    p = UploadImage(image=base, style=style)
    p.save()

    hoge = "upload success"
    
    return HttpResponse(hoge)
