from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'product_name',
        'is_tax',
        'pdf_file',
        'image_file',
        'feature',
    ]

    list_display_links = ['pk','product_name',]
    
    list_filter = ['is_tax']
    
    search_fields = ['product_name']