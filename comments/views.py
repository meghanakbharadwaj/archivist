from django.shortcuts import render
from archivist_app.models import Course
from .models import Comment

# Create your views here.

def comments(request,course_id):
    course = Course.objects.get(id = course_id)
    comments = Comment.objects.filter(course_id = course_id)
    return render(request,'comments.html',{'course':course,'comments':comments,})