
from django.contrib import admin
from .models import Quote, QuoteItem, EmailHistory


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    """
    Quote admin setting
    """
    list_display = (
        'pk',
        'organ',
        'user_creator',
        'created_at',
    )
    list_display_links = (
        'pk',
        'organ',
    )
    search_fields = (
        'organ__icontains',
    )
    list_filter = (
        'user_creator',
        'created_at',
    )


@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    """
    Quote Item admin setting
    """
    list_display = (
        'pk',
        'quote',
        'product',
        'price',
        'quantity',
        'discount',
    )
    list_display_links = (
        'pk',
        'quote',
    )
    list_filter = (
        'product',
    )
    search_fields = (
        'quote__icontains',
        'product__icontains',
    )
    list_editable = (
        'price',
        'quantity',
        'discount',
    )

@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'quote',
        'status',
        'email',
        'user_creator',
        'created_at',
    )

    list_filter = (
        'quote',
        'status',
        'email',
        'user_creator',
    )

    search_fields = (
        'quote',
    )