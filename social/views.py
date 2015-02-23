from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render(request, 'index.html')



# Create your views here.
