from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    """A view to return the index page """
    return render(request, 'index.html')






