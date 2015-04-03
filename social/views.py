from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from social.models import Content, UserPic
from social.forms import User_Content, User_form, User_pic_form
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from serializers import ContentSerializer
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def content(request):
    if request.method == 'GET':
        content1 = Content.objects.order_by('?').all()
        serializer = ContentSerializer(content1, many=True)
        return JSONResponse(serializer.data)

def splash(request):
    error = ""
    if request.method == 'POST':
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
    if len(request.GET)==0:
        return render(request, "index.html", {'currentUser': request.user.username})
    else:
        searchFilter = request.GET['searchFilter']
        if searchFilter=='tag':
            searchFor = request.GET['searchFor']
            searchFor = [x.lower() for x in [searchFor]]
            searchFor =searchFor[0].split()
            return render(request, "index.html", {'posts': Content.objects.filter(tags__name__in=searchFor).distinct(), 'currentUser': request.user.username})

        # Just here until other cases are implemented
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
        form = User_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else: 
        form = User_form()
    return render(request, 'signup.html', {'form': form})

def about(request):
    return render(request, "about.html", {'currentUser': request.user.username})

@login_required(login_url='/')
def userpic(request):
    if request.method == 'POST':
        # we need to process data
        form = User_pic_form(request.POST)
        if(form.is_valid()):
            form.save(commit = True)
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'userpic.html', {'form': form, 'currentUser': request.user.username})
    else:
        # create blank form
        form = User_pic_form()
        return render(request, 'userpic.html', {'form': form, 'currentUser': request.user.username})

@login_required(login_url='/')
def profile(request):
    try:
        pic = UserPic.objects.get(username = request.user.username)
    except UserPic.DoesNotExist:
        pic = None

    return render(request, "profile.html", {'currentUser': request.user.username, 'pic': pic, 'person': User.objects.get(username = request.user.username ), "posts":Content.objects.filter(username = request.user.username ).order_by('datetime')})