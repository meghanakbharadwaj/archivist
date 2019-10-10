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

def courses(request):
    courses = Course.objects.all().filter(keyword__keyword = 'Python')
    #courses = Course.objects.all()
    return render(request,'courseList.html',{'courses' : courses})

#def courseLink(request):
#    course = Course.objects.get(id = 1)
#    return render(request,course.course_link)