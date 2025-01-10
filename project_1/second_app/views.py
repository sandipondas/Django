from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(response):
    return HttpResponse("Courses page")
