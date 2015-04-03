from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from social.models import Content, UserPic
from social.forms import UserContent, UserForm, UserPicForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from serializers import ContentSerializer
from rest_framework import permissions

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.order_by('?').all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@csrf_exempt
def pin(request):
    content = Content.objects.get(pk=request.POST.get('pk'))
    try:
        Content.objects.get(image=content.image, username=request.user.username)
    except Content.DoesNotExist:
        my_content = Content()
        my_content.url = content.url
        my_content.description = content.description
        my_content.image = content.image
        my_content.tags = content.tags
        my_content.username = request.user.username
        my_content.save()
    response = {"success": "true"}
    return JSONResponse(response)


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
            error = "Username/Password is not valid."
    return render(request, 'login.html', {'error': error})


def dashboard(request):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    if len(request.GET) == 0:
        return render(request, "index.html", {'navigation': navigation, 'currentUser': request.user.username})
    else:
        term = request.GET['searchFilter']
        if term == 'tag':
            search = request.GET['searchFor']
            search = [x.lower() for x in [search]]
            search = search[0].split()
            return render(request, "index.html", {'posts': Content.objects.filter(tags__name__in=search).distinct(),
                                                  'currentUser': request.user.username})
        # Just here until other cases are implemented
        return render(request, "index.html", {'navigation': navigation, 'posts': Content.objects.order_by('?').all(),
                                              'currentUser': request.user.username})


@login_required(login_url='/')
def new_post(request):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    if request.method == 'POST':
        # we need to process data
        form = UserContent(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'new_post.html', {'form': form, 'currentUser': request.user.username})
    else:
        # create blank form
        form = UserContent()
        return render(request, 'new_post.html', {'navigation': navigation, 'form': form, 'currentUser': request.user.username})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'navigation': navigation, 'form': form})


def about(request):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    return render(request, "about.html", {'currentUser': request.user.username, 'navigation': navigation})


@login_required(login_url='/')
def userpic(request):
    if request.method == 'POST':
        # we need to process data
        form = UserPicForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'userpic.html', {'form': form, 'currentUser': request.user.username})
    else:
        # create blank form
        form = UserPicForm()
        return render(request, 'userpic.html', {'form': form, 'currentUser': request.user.username})


def users(request, username):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    try:
        pic = UserPic.objects.get(username=username)
    except UserPic.DoesNotExist:
        pic = None
    try:
        person = User.objects.get(username=username)
    except User.DoesNotExist:
        person = None
    return render(request, 'users.html', {'person': person, 'navigation': navigation, 'pic': pic,
                                          'currentUser': request.user.username,
                                          'posts': Content.objects.filter(username=username).order_by('datetime')[:5]})


@login_required(login_url='/')
def profile(request):
    if request.user.is_authenticated():
        navigation = True
    else:
        navigation = False
    try:
        pic = UserPic.objects.get(username=request.user.username)
    except UserPic.DoesNotExist:
        pic = None

    return render(request, "profile.html", {'currentUser': request.user.username,
                                            'navigation': navigation, 'pic': pic,
                                            'person': User.objects.get(username=request.user.username),
                                            'posts': Content.objects.filter(username=request.user.username).order_by('datetime')})
