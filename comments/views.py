from django.shortcuts import render,redirect
from archivist_app.models import Course
from .models import Comment
from django.contrib import messages

import re
# Create your views here.

def comments(request,course_id):
    course = Course.objects.get(id = course_id)
    comments = Comment.objects.filter(course_id = course_id, parent = None).order_by('-timestamp')
    return render(request,'comments.html',{'course':course,'comments':comments,})

def postComment(request,course_id,parent_id=None):
    user_id = request.user.id
    if user_id is None:
        messages.info(request,'You must login to comment or reply\n Login and try again!',extra_tags='danger')
        return redirect('comments',course_id)
    user_input = request.POST.get('content_data').strip()
    if re.search('\S+',user_input):
        new_comment = Comment.objects.get_or_create(
            user = request.user,
            content = user_input,
            course_id = course_id,
            parent_id = parent_id
        )
        messages.info(request,'Your comment or reply was posted',extra_tags='success')
        return redirect('comments',course_id)
    else:
        messages.info(request,'Your comment or reply was empty!  Type something and try again',extra_tags='danger')
        return redirect('comments',course_id)
        