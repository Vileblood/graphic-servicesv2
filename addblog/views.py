from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.


def addblog(request):
    """A view to return add blog page"""
    return render(request, 'addblog.html')

    