
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products
from authentication import views
from django.shortcuts import render
from .models import Products

def signout(request):
    """
    This view function renders the signout page.
    """
    # Get the current value of the 'count' cookie,
    count = int(request.COOKIES.get('count', 0))
    
    # Increment the count
    count += 1
    
    # Set the updated 'count' cookie in the response
    response = render(request, 'signout.html', {'value': Products.objects.all(), 'count': count})
    response.set_cookie('count', count)
    
    # Print cookies for debugging
    print(request.COOKIES, "Hello")
    
    return response



