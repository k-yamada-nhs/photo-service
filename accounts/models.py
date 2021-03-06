from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    profileimage = models.ImageField(upload_to='profileimage')
    comment =models.TextField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profileimage)
