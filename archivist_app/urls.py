from django.urls import path
from archivist_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.homeView,name = 'home'),
    #path('',views.addCourseView,name = 'addCourse'),
    path('courses',views.categories,name = 'categories'),
    path('courses/(?P<key>[-a-zA-Z0-9_]+)$',views.courses,name='courses'),
    path('courseLink/(?P<course_name>)',views.courseLink,name='courseLink'),
    path('login',views.login,name='login')
]