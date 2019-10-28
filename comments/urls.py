from django.urls import path
from comments import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<course_id>/',views.comments,name='comments'),
    path('postComment/<course_id>/',views.postComment,name='postComment'),
    path('postComment/<course_id>/<parent_id>',views.postComment,name='postComment')
]
