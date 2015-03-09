from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Content(models.Model):
    url = models.URLField()
    description = models.TextField(max_length = 200)
    username = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.URLField()