from django.urls import path, include
from . import views
# specify the path
urlpatterns = [
    path('products',views.products_page,name='products'),
]
