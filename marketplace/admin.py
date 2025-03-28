from django.contrib import admin
from .models import Artwork # Import your new Artwork model

# Register your models here.

@admin.register(Artwork) # Use the @admin.register decorator (cleaner way)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'created_at') # Columns to show in the list view
    list_filter = ('artist', 'created_at') # Filters available in the sidebar
    search_fields = ('title', 'description') # Fields to search through
    # readonly_fields = ('created_at', 'updated_at') # If you want these non-editable