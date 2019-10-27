from django.urls import path
from comments import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<course_id>/',views.comments,name='comments'),
    
]
