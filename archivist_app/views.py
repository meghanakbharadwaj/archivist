from django.shortcuts import render
from django.http import HttpResponse
from archivist_app.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def homeView(request):
    return render(request,'home.html')

def addCourseView(request):
    return render(request,'addCourse.html')


def categories(request):
    keywords = Keywords.objects.all()
    return render(request,'categories.html',{'keywords':keywords})

