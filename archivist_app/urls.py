from django.urls import path
from archivist_app import views

urlpatterns = [
    #path('',views.homeView,name = 'home')
    path('',views.addCourseView,name = 'addCourse')
]