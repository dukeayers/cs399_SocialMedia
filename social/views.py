from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from social.models import UserLogin, User
def home(request):
    error = ""
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username = username, password = password).count() == 1:
                return HttpResponse("Good")
            else:
                error = "Username/Password is incorrect."
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form, 'error': error})



# Create your views here.
