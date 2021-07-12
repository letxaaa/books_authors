from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    return HttpResponse(request,"Hello there!")