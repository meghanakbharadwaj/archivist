from django.shortcuts import render,redirect
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

def courses(request,key):
    courses = Course.objects.all().filter(keyword__keyword = key)
    #courses = Course.objects.all()
    return render(request,'courseList.html',{'courses' : courses})

def courseLink(request,course_name):
    course = Course.objects.get(title = course_name)
    return redirect(course.course_link)
