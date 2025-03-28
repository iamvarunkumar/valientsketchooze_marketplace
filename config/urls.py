# config/urls.py (CORRECTED urlpatterns)
from django.contrib import admin
from django.urls import path, include # Make sure include is imported
from django.conf import settings
from django.conf.urls.static import static

# REMOVE any 'views' imports here

urlpatterns = [
    # Project-wide paths:
    path('admin/', admin.site.urls),                        # Admin site
    path('accounts/', include('django.contrib.auth.urls')), # Built-in auth (login, logout etc)

    # Include URLs from the marketplace app:
    path('', include('marketplace.urls')), # This connects to marketplace/urls.py
]

# This part for serving media files in DEBUG is correct
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)