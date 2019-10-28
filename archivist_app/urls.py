from django.urls import path
from archivist_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.homeView,name = 'home'),
    path('categories/<dom>/',views.categories,name = 'categories'),
    path('courses/<key>/',views.courses,name='courses'),
    path('courseLink/<course_name>/',views.courseLink,name='courseLink'),
    path('search',views.search,name='search'),
    #path('upvote/(?P<course_title>[-a-zA-Z0-9_]+)/(?P<keyword>[-a-zA-Z0-9_]+)$',views.upvote,name='upvote'),
    path('upvote/<course_title>/<keyword>',views.upvote,name='upvote'),

    #path('upvote/\\(\\?P(?P<course_name>[^/]+)\\\\s\\+\\)/\\(\\?P(?P<keyword>[^/]+)\\\\s\\+\\)/\\(\\?P(?P<user_id>[^/]+)\\\\s\\+\\)\\$$',views.upvote,name='upvote')
]


