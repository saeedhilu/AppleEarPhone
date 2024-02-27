
from typing import Any
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
class RestrictAdminUserInFrontend:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin panel and the user is a regular user
        if request.path.startswith('/admin/') and not request.user.is_superuser and request.user.is_authenticated:
            messages.error(request, "Access denied. Only superusers are allowed to access the admin panel.")
            return redirect('products')                                            
        
        response = self.get_response(request)
        return response
    
# class RestrictAdminFromBackend:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):    
#         # Check if the user is a superuser and the request is for the frontend
#         if not request.path.startswith('/admin/') and  request.user.is_superuser and request.user.is_authenticated:
#             # Redirect superusers to the admin panel
#             return redirect('/admin/')
#         response = self.get_response(request)
#         return response
    
    
