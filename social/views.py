from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from social.models import Content
from social.forms import User_Content, UserForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/')
def dashboard(request):
    return render(request, "index.html", {'posts': Content.objects.order_by('?').all(), 'currentUser': request.user.username})

@login_required(login_url='/')
def new_post(request):
    if request.method == 'POST':
        # we need to process data
        form = User_Content(request.POST)
        if(form.is_valid()):
            form.save(commit = True)
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'new_post.html', {'form': form, 'currentUser': request.user.username})
    else:
        # create blank form
        form = User_Content()
        return render(request, 'new_post.html', {'form': form, 'currentUser': request.user.username})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thankyou')
    else: 
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def about(request):
    return render(request, "about.html", {'currentUser': request.user.username})

def profile(request):
    return render(request, "profile.html", {'currentUser': request.user.username, 'person': User.objects.get(username = request.user.username ), "posts":Content.objects.filter(username = request.user.username ).order_by('datetime')})