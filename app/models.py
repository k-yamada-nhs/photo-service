from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Photo(models.Model):
    
    # タイトル
    title = models.CharField(max_length=150)
    # コメント
    comment = models.TextField(blank=True)
    # ベース画像
    baseimagepath = models.CharField(max_length=150)
    # スタイル
    styleimagepath = models.CharField(max_length=150)
    # 出力
    outputimagepath = models.CharField(max_length=150)
    # 緯度
    latitude = models.CharField(max_length=150, null=True)
    # 経度
    longitude = models.CharField(max_length=150, null=True)
    # ユーザーインスタンスを削除した際投稿も削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 作成日
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Relationship(models.Model):

    # フォロー
    follow = models.ForeignKey(User, related_name='follow', on_delete=models.CASCADE)
    # フォロワー
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.follow.username, self.follower.username)

class Comnt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    target = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="photo")

    def __str__(self):
        return self.text

class Reply(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    target = models.ForeignKey(Comnt, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username