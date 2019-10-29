from django.urls import path
from archivist_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.homeView,name = 'home'),
    path('categories/<dom>/',views.categories,name = 'categories'),
    path('courses/<key>/',views.courses,name='courses'),
    path('courseLink/<course_name>/',views.courseLink,name='courseLink'),
    path('search',views.search,name='search'),
    path('upvote/<course_title>/<keyword>/',views.upvote,name='upvote'),
]


