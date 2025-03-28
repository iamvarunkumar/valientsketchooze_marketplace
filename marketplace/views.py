from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages # Optional: for success messages
from .models import Artwork

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new user
            username = form.cleaned_data.get('username') # Optional
            messages.success(request, f'Account created for {username}! You can now log in.') # Optional
            return redirect('login') # Redirect to the login page after successful signup
    else: # GET request
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Add a placeholder for home view if needed by base.html link
def home(request):
    artworks = Artwork.objects.all() # Fetch artworks
    # CORRECTED LINE: Render 'home.html' (or 'gallery.html') and pass context
    return render(request, 'home.html', {'artworks': artworks})

def artwork_detail(request, pk):
    # Retrieve the specific artwork object using its primary key (pk)
    # If not found, automatically raises a 404 Page Not Found error
    artwork_obj = get_object_or_404(Artwork, pk=pk)

    # Prepare the context dictionary to pass the artwork object to the template
    context = {
        'artwork': artwork_obj
    }
    # Render the detail template, passing the context
    return render(request, 'artwork_detail.html', context)

# Add home view to marketplace/urls.py: path('', views.home, name='home')