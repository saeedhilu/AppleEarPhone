
from django.contrib import admin
from django.urls import path, include
from . import views
# specify the path
urlpatterns = [
    
    path('', views.home, name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout_btn,name='logout'),
    
]
