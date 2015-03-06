from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

# Create your models here.
class Content(models.Model):
    url = models.URLField()
    description = models.TextField(max_length = 200)
    username = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.URLField()

class User_Content(ModelForm):
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Website URL'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Description'}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Image URL'}))
    username = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Content
        fields = ['url', 'description', 'image', 'username']
        
        