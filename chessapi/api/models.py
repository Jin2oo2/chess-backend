from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    rating = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)


class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    date_played = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=30, default="no result")
    level = models.CharField(max_length=15, default="easy")
