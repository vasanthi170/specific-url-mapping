from django.shortcuts import render
from django.http import*


def captain(request):
    return HttpResponse('<h1> X is the captain of RCB</h1>')
