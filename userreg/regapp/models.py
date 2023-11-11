
from django.db import models

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/')

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)

