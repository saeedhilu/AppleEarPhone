# from django.contrib.auth import authenticate, login, logout  
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.shortcuts import redirect, render
# import re




# def home(request):
#     """
#     Renders the signup page if the user is not authenticated. If the 
#     user is authenticated, it redirects to the product_page page.
#     """
#     if request.user.is_authenticated:
#         return redirect('product_page')
    
#     return render(request, 'signup.html')

# def signup(request):
    
#     """
#     Handles user registration. Validates the provided username and 
#     passwords, checks for username availability, and creates a new 
#     user if all conditions are met.
#     """
#     if request.user.is_authenticated:
#         return redirect(home)
#     if request.method == "POST":
#         # Assigning the values
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
        

#         # This is for username exists or not
#         # This is for checking password length > 8
        
#         if len(pass1) < 8:
#             messages.error(request,'Password atleast 8 characters')
#             return redirect('signup')
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return redirect('signup')

#         # This is for cheking username is not lengthy
#         if len(username) > 10:
#             messages.error(request, "Username should be less than 10 characters.")
#             return redirect('signup')
# # check username is numbers and letters only
#         if not re.match("^[a-zA-Z0-9]+$", username):
#             messages.error(request, "Username should contain only letters (a-z, A-Z) or numbers (0-9).")
            
#             return redirect('signup')

#         # This is for password checking
#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')
        
#         # saving purposes
#         myuser = User.objects.create_user(username=username, password=pass1)
#         myuser.save()
#         # Redirect to the signin page after successful signup
#         return redirect('signin')

#     return render(request, 'signup.html')

# def signin(request):
#     """
#     Handles user login. Authenticates the user with the provided 
#     credentials and redirects to the home page upon successful login.
#     Displays an error message if authentication fails.
#     """
#     if request.user.is_authenticated:
#         return redirect(home)  # Redirect to home page if already logged in
    
#     if request.method == "POST":
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username, password=pass1)

#         # Check user is valid or not
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home page after successful login
        
#         # User is not valid
#         else:
#             messages.error(request,"Invalid username or password. Please try again.")
#             return redirect('signin')

#     return render(request, 'signin.html')

# def logout_btn(request):
#     """
#     Logs out the current user and redirects to the signin page. It also
#     deletes a specific cookie named 'count' if it exists.
#     """
#     logout(request)
#     response = redirect('signin')
#     response.delete_cookie('count')
#     return response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
import re


@never_cache
def home(request):
    """
    Renders the signup page if the user is not authenticated. If the 
    user is authenticated, it redirects to the product_page page.
    """
    if request.user.is_authenticated:
            return redirect('products')
    
    return render(request, 'signup.html')
@never_cache
def signup(request):
    """
    Handles user registration. Validates the provided username and 
    passwords, checks for username availability, and creates a new 
    user if all conditions are met.
    """
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == "POST":
        # Assigning the values
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # This is for checking password length > 8
        
        if len(pass1) < 8:
            messages.error(request,'Password must be at least 8 characters long')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # This is for checking if the username is not too lengthy
        if len(username) > 10:
            messages.error(request, "Username should be less than 10 characters.")
            return redirect('signup')

        # Check if username contains only letters and numbers
        if not re.match("^[a-zA-Z0-9]+$", username):
            messages.error(request, "Username should contain only letters (a-z, A-Z) or numbers (0-9).")
            return redirect('signup')

        # This is for password checking
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        # Create user
        myuser = User.objects.create_user(username=username, password=pass1)

        myuser.save()
        return redirect('signin')

    return render(request, 'signup.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .views import home

@never_cache
def signin(request):
    """
    Handles user login. Authenticates the user with the provided 
    credentials and redirects to the home page upon successful login.
    Displays an error message if authentication fails.
    """
    if request.user.is_authenticated:
        return redirect(home)  # Redirect to home page if already logged in
    
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        # Check user is valid or not
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        
        # User is not valid
        else:
            messages.error(request,"Invalid username or password. Please try again.")
            return redirect('signin')

    return render(request, 'signin.html')


def logout_btn(request):
    """
    Logs out the current user and redirects to the signin page. It also
    deletes a specific cookie named 'count' if it exists.
    """
    logout(request)
    request.session.flush()  # Clear any session data
    response = redirect('signin')
    response.delete_cookie('count')
    return response