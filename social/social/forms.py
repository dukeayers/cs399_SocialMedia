from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from social.models import Content, UserPic

class User_Content(forms.ModelForm):
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Website URL'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Description'}))
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Image URL'}))
    username = forms.CharField(widget=forms.HiddenInput())
    tags = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Separate Tags by a Comma'})

    class Meta:
        model = Content
        fields = ['url', 'description', 'image', 'username', 'tags']

class User_form(UserCreationForm):  
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class User_pic_form(forms.ModelForm):
	username = forms.CharField(widget=forms.HiddenInput())
	url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Picture URL'}))
	
	class Meta:
		model = UserPic
		fields = ['username', 'url']
	