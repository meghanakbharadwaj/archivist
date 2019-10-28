from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from archivist_app.models import *
from django.db.models import Max
from django.contrib import messages
from comments.models import Comment

# Create your views here.
def home(request):
    return render(request,'home.html')

def homeView(request):
    return render(request,'home.html')

def addCourseView(request):
    return render(request,'addCourse.html')


def categories(request,dom):
    if dom != 'all':
        keywords = Keywords.objects.all().filter(domain__domain_name = dom)
    else:
        keywords = Keywords.objects.all()
    return render(request,'categories.html',{'keywords':keywords})

def courses(request,key):
    keyword = Keywords.objects.all().filter(keyword = key)[0]
    courses = Course.objects.all().filter(keyword__keyword = key).order_by('-votes')
    commentCount = []
    for course in courses:
        commentCount.append(len(Comment.objects.all().filter(course_id = course.id,parent=None)))
    #courses = Course.objects.all()
    countList = zip(courses,commentCount)
    return render(request,'courseList.html',{'countList' : countList, 'keyword':keyword})

def courseLink(request,course_name):
    course = Course.objects.get(title = course_name)
    return redirect(course.course_link)

def login(request):
    return render(request,'login.html')

def search(request):
    keywords = Keywords.objects.filter(keyword__icontains=request.GET.get('search'))
    courses = Course.objects.filter(title__icontains = request.GET.get('search')).order_by('-votes')
    commentCount = []
    for course in courses:
        commentCount.append(len(Comment.objects.all().filter(course_id = course.id,parent=None)))
    countList = zip(courses,commentCount)
    if not courses:
        countList = None 
    return render(request,'search.html',{'keywords':keywords,'countList':countList})

def upvote(request,course_title,keyword):
    user_id = request.user.id
    courses = Course.objects.all().filter(keyword__keyword = keyword).order_by('-votes')
    if user_id is None:
        messages.info(request,'You must login to upvote a course\n Try to Login!',extra_tags='login_required')
        # return render(request,'courseList.html',{'courses' : courses})
        return redirect('courses',key=keyword)
    else:
        user = User.objects.get(id = user_id)
        course = Course.objects.filter(title = course_title)
        course_object = Course.objects.get(title = course_title)
        vote_count = course.values('votes')
        votes =  Upvote.objects.filter(course__title = course_title,user__id = user_id).exists()

        if not votes:
            course.update(votes=int(vote_count[0]['votes'])+1)
            Upvote.objects.create(user = user,course = course_object)
        else:
            messages.info(request,"You've already upvoted this course.",extra_tags='login_required')
        courses = Course.objects.all().filter(keyword__keyword = keyword).order_by('-votes')
        # return render(request,'courseList.html',{'courses' : courses})
        return redirect('courses',key=keyword)
