# marketplace/urls.py (CORRECTED)
from django.urls import path
from . import views # Use relative import within the app

app_name = 'marketplace' # This defines the namespace

urlpatterns = [
    # Paths specific to the marketplace app:
    path('', views.home, name='home'),          # Homepage/Gallery
    path('signup/', views.signup, name='signup'), # Signup page
    # Add artwork_detail path later:
    path('artwork/<int:pk>/', views.artwork_detail, name='artwork_detail'),
]