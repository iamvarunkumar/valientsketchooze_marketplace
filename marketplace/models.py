from django.db import models
from django.conf import settings # Required to link to the User model correctly

class Artwork(models.Model):
    # --- Core Artwork Details ---
    title = models.CharField(max_length=200, help_text="The title of the artwork.")
    description = models.TextField(blank=True, null=True, help_text="A detailed description of the artwork (optional).")
    price = models.DecimalField(
        max_digits=10,        # Allows prices up to 99,999,999.99
        decimal_places=2,     # Stores price with 2 decimal places (e.g., for Rupees/Paisa)
        help_text="Price in INR."
    )
    # --- File & Artist ---
    # Requires Pillow library: pip install Pillow
    image = models.ImageField(
        upload_to='artworks/', # Files will be saved in MEDIA_ROOT/artworks/ directory
        help_text="The main image file for the artwork."
    )
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,     # Links to the built-in User model
        on_delete=models.CASCADE,     # If the artist User is deleted, delete their artwork too
        related_name='artworks',      # Allows accessing user.artworks easily
        help_text="The artist who uploaded this artwork."
    )
    # --- Timestamps ---
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)     # Automatically set when saved

    # --- Representation ---
    def __str__(self):
        # How the artwork object will be represented (e.g., in the admin)
        return f"{self.title} by {self.artist.username}"

    class Meta:
        ordering = ['-created_at'] # Optional: Default order artworks by newest first