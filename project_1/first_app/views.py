from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(response):
    return HttpResponse("Courses page")

def about(response):
    return HttpResponse("about page")

def home(response):
    return HttpResponse("home page")