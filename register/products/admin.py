from django.contrib import admin

from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','image']  # Use square brackets for list

admin.site.register(Products, ProductAdmin)  # Register the model with the custom admin class
