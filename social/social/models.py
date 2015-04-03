from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Content(models.Model):
    url = models.URLField()
    description = models.TextField(max_length=200)
    username = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    tags = TaggableManager(blank=True)


class UserPic(models.Model):
    username = models.CharField(max_length=30)
    url = models.URLField()
