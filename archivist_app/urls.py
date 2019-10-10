from django.urls import path
from archivist_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    #path('',views.homeView,name = 'home')
    #path('',views.addCourseView,name = 'addCourse'),
    path('',views.categories,name = 'categories'),
    path('courses',views.courses,name='courses'),
    #path('courseLink',RedirectView.as_view(url=''))
]