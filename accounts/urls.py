from django.urls import path
from accounts import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signUp,name = 'signup'),
    
]


