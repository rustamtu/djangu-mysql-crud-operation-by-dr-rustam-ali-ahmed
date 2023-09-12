from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse

# from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    data = {
        'static_link': '/static/template1_src',
        'name': 'Rustam Ali Ahmed',
    }
    return render(request, "html_pages/home.html", data)

def about(request):
    data = {
        'static_link': '/static/template1_src',
        'name': 'Rustam Ali Ahmed',
    }
    return render(request, "html_pages/about.html", data)

def contact(request):
    data = {
        'static_link': '/static/template1_src',
        'name': 'Rustam Ali Ahmed',
    }
    return render(request, "html_pages/contact.html", data)

def raa(request):
    return HttpResponse("Hello, world. You're at the polls raa function.")