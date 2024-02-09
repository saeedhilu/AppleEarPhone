from django.urls import path, include
from . import views
# specify the path
urlpatterns = [
    path('signout',views.signout,name='signout'),

]
