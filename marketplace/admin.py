from django.contrib import admin
from .models import Artwork, Order # Import your new Artwork model

# Register your models here.

@admin.register(Artwork) # Use the @admin.register decorator (cleaner way)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'created_at') # Columns to show in the list view
    list_filter = ('artist', 'created_at') # Filters available in the sidebar
    search_fields = ('title', 'description') # Fields to search through
    readonly_fields = ('created_at', 'updated_at') # If you want these non-editable

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'artwork_title', 'amount', 'status', 'provider_order_id', 'created_at')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ('user__username', 'artwork__title', 'provider_order_id', 'payment_id')
    # Make most fields read-only in admin, as they are set by the system/payment flow
    readonly_fields = ('user', 'artwork', 'amount', 'provider_order_id', 'payment_id', 'signature', 'created_at')
    list_per_page = 20 # Optional: Show more orders per page

    # Helper method to display artwork title nicely
    def artwork_title(self, obj):
        if obj.artwork:
            return obj.artwork.title
        return '-'
    artwork_title.short_description = 'Artwork Title' # Column header

    # Prevent creating Orders directly via Admin interface
    def has_add_permission(self, request):
        return False

    # Optional: Prevent deletion too? Maybe allow for cleanup during dev.
    def has_delete_permission(self, request, obj=None):
        return False   