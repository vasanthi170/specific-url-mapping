from django.shortcuts import render
from django.http import*


def captain(request):
    return HttpResponse('<h1>Virat Kohli is the captain of RCB</h1>')

# Create your views here.
