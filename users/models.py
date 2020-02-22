from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profilepic.jpg', upload_to='profile_pic')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

