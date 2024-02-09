from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  # Include authentication app URLs
    path('products/', include('products.urls')),  # Include products app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
