from django.core.cache import cache
from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from .models import Products

# def cache_saving():
#     """
#     Fetches the products either from the cache or the database,
#     and caches the result with a timeout if not already in the cache.
#     """
#     cache_values = cache.get('cache_values')

#     if cache_values is None:
#         cache_values = Products.objects.all()
#         cache.set('cache_values', cache_values, timeout=30)  # Set timeout to 30 seconds
#         print("Fetched from database and cached.")
#     else:
#         print("Fetched from cache.")

#     return cache_values


@never_cache
def products_page(request):
    # import os
    # import redis

    # # Connect to your internal Redis instance using the REDIS_URL environment variable
    # # The REDIS_URL is set to the internal Redis URL e.g. redis://red-343245ndffg023:6379
    # r = redis.from_url(os.environ['REDIS_URL'])

    # r.set('key', 'redis-py')
    # r.get('key')
    if not request.user.is_authenticated:
            return redirect('signin')
    # Get the current value of the 'count' cookie, defaulting to 0 if it doesn't exist
    count = int(request.COOKIES.get('count', 0))
    
    # Increment the count
    count += 1
    cache_values = Products.objects.all()
    # Retrieve the product list from the cache or database
    product_list = cache_values
    
    # Set the updated 'count' cookie in the response
    response = render(request, 'products.html', {'value': product_list, 'count': count})
    response.set_cookie('count', count)
    
    # print(request.COOKIES)
    return response

    
