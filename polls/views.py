from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse

# from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return HttpResponse("polls->home")

def raa(request):
    return HttpResponse("Hello, world. You're at the polls raa function.")