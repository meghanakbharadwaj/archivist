from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request,'home.html')

def addCourseView(request):
    return render(request,'addCourse.html')