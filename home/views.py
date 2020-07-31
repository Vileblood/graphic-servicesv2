from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    """A view to return the index page """
    return HttpResponse(request, 'home/index.html')

def addblog(request):
    """A view to return the addblog page """
    return HttpResponse(request, 'addblog/addblog.html')




