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
    artworks = Artwork.objects.all()
    print("Artworks fetched in home view:", artworks) # <-- ADD PRINT
    return render(request, 'home.html', {'artworks': artworks})

def artwork_detail(request, pk):
    artwork_obj = get_object_or_404(Artwork, pk=pk)
    print("Artwork fetched in detail view:", artwork_obj) # <-- ADD PRINT
    context = {'artwork': artwork_obj}
    return render(request, 'artwork_detail.html', context)

# Add home view to marketplace/urls.py: path('', views.home, name='home')