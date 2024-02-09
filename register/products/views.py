# from turtle import home
# from django.shortcuts import render,redirect
# from .models import Products
# from authentication import views

# # Create your views here.
# def signout(request):
    
#     dict_images = {
#         'value': Products.objects.all()
#     }
#     return render(request, 'signout.html', dict_images)
# def signin(request):
#     if request.user.is_authenticated:
#         return redirect('home') 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products
from authentication import views

# Constant for the cookie name

from django.shortcuts import render
from .models import Products

def signout(request):
    # Get the current value of the 'count' cookie, defaulting to 0 if it doesn't exist
    count = int(request.COOKIES.get('count', 0))
    
    # Increment the count
    count += 1
    
    # Set the updated 'count' cookie in the response
    response = render(request, 'signout.html', {'value': Products.objects.all(), 'count': count})
    response.set_cookie('count', count)
    
    # Print cookies for debugging
    print(request.COOKIES, "Hello")
    
    return response



