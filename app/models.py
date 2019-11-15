from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
<<<<<<< HEAD
    image = models.ImageField(upload_to='photos')
=======


    baseimagepath = models.CharField(max_length=150)
    styleimagepath = models.CharField(max_length=150)

    outputimagepath = models.CharField(max_length=150)

>>>>>>> 94fe32d80ea0888419e007f277db2fbdc865aeba
    # ユーザーインスタンスを削除した際投稿も削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Relationship(models.Model):
    follow = models.ForeignKey(User, related_name='follow', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.follow.username, self.follower.username)

class UploadImage(models.Model):
    image = models.ImageField(upload_to='base')
    style = models.ImageField(upload_to='style')