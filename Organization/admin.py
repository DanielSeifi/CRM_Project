from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'state',
        'name',
        'phone',
        'workers_qty',
        'full_name_owner',
        'phone_owner',
        'email_owner',
        'created_at',
        'user_creator',
    ]

    list_filter = ['state', 'organ_product', 'user_creator', ]

    list_display_links = ['pk', 'name', ]

    list_per_page = 5

    search_fields = ['name', ]
