from django.db import models
from django.forms import ModelForm
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 40)
    email_address = models.EmailField(max_length = 40)

class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']