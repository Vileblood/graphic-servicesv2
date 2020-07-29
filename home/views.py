from django.shortcuts import render

def index(request):
    """A view to return the index page """
    return render(request, 'home/index.html')

def addblog(request):
    """A view to return add blog page"""
    return render(request, 'addblog/addblog.html')


