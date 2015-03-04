from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from social.models import Content, User_Content
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
def splash(request):
    error = ""
    if request.method == 'POST':
        # form = UserLogin(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("here")
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            error="Username/Password is not valid."
    return render(request, 'login.html', {'error': error})


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, "index.html", {'posts': Content.objects.all(), 'currentUser': request.user.username})
    else:
        return HttpResponseRedirect('/')

def new_post(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            # we need to process data
            form = User_Content(request.POST)
            form.datetime = datetime.now()
            form.username = request.user.username
            if(form.is_valid()):
                form.save(commit = True)
                return HttpResponseRedirect('/dashboard')
            else:
                return render(request, 'new_post.html', {'form': form, 'currentUser': request.user.username})
        else:
            # create blank form
            form = User_Content()
            return render(request, 'new_post.html', {'form': form, 'currentUser': request.user.username})
    else:
        # they aren't logged in
        return HttpResponseRedirect('/')    

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
