# marketplace/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings # To access API keys
from django.contrib.auth.decorators import login_required # To ensure user is logged in
from django.views.decorators.http import require_POST # To ensure only POST requests
from .models import Artwork, Order # Import models
from django.contrib import messages
import razorpay

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

@login_required # Decorator to ensure user is logged in
@require_POST # Decorator to ensure this view only accepts POST requests
def initiate_payment(request):
    # --- 1. Get Data & Validate ---
    artwork_id = request.POST.get('artwork_id')
    if not artwork_id:
        # Handle error: artwork_id not provided
        # Maybe redirect back with an error message?
        return redirect('marketplace:home') # Redirect home for now

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    user = request.user
    amount_in_paisa = int(artwork.price * 100) # Convert amount to smallest unit (Paisa for INR)

    # --- 2. Create Local Order (PENDING) ---
    # Use update_or_create if you want to reuse pending orders,
    # but creating new is simpler for now.
    try:
        order = Order.objects.create(
            user=user,
            artwork=artwork,
            amount=artwork.price, # Store original amount
            status=Order.STATUS_PENDING
            # provider_order_id will be updated below
        )
    except Exception as e:
        # Handle potential DB error during order creation
        print(f"DB Error creating order: {e}")
        # return render(request, 'payment_failed.html', {'error': 'Could not initiate order.'})
        return redirect('marketplace:home') # Redirect home for now

    # --- 3. Create Razorpay Order ---
    try:
        # Initialize Razorpay client (using TEST keys from settings)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # Or if you used RAZORPAY_... names in settings:
        # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


        # Data for Razorpay's order creation API
        razorpay_order_data = {
            'amount': amount_in_paisa,
            'currency': 'INR',
            'receipt': f'order_rcptid_{order.id}', # Use our local Order ID as a unique receipt ID
            'notes': { # Optional: Add helpful notes
                'artwork_id': artwork.id,
                'artwork_title': artwork.title,
                'user_id': user.id,
                'email': user.email
            }
        }

        # Create the order on Razorpay's side
        razorpay_order = client.order.create(data=razorpay_order_data)

        # --- 4. Update Local Order with Razorpay Order ID ---
        order.provider_order_id = razorpay_order['id']
        order.save()

    except razorpay.errors.BadRequestError as e:
        # Handle specific Razorpay API errors (e.g., invalid amount)
        print(f"Razorpay Bad Request Error: {e}")
        order.status = Order.STATUS_FAILED
        order.save()
        # return render(request, 'payment_failed.html', {'error': 'Payment gateway error.'})
        return redirect('marketplace:home')
    except Exception as e:
        # Handle other generic errors (network issues, etc.)
        print(f"General Error creating Razorpay order: {e}")
        order.status = Order.STATUS_FAILED # Mark local order as failed
        order.save()
        # return render(request, 'payment_failed.html', {'error': 'Could not connect to payment gateway.'})
        return redirect('marketplace:home')

    # --- 5. Prepare Context for Checkout Template ---
    context = {
        'razorpay_key_id': settings.RAZORPAY_KEY_ID, # Or settings.RAZORPAY_KEY_ID
        'razorpay_order_id': razorpay_order['id'],
        'amount': amount_in_paisa,
        'currency': 'INR',
        'artwork_title': artwork.title,
        'user_name': user.get_full_name() or user.username,
        'user_email': user.email,
        'user_contact': '', # Add user phone if available
        'artwork': artwork,
    }

    # --- 6. Render Checkout Template ---
    return render(request, 'payment_checkout.html', context)
