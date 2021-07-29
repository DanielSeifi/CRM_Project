from django import forms
from . import models


class OrganForm(forms.ModelForm):
    model = models.Organization

    class Meta:
        fields = [
            'state',
            'name',
            'phone',
            'workers_qty',
            'organ_product',
            'full_name_owner',
            'phone_owner',
            'email_owner',
            'created_at',
            'user_creator',
        ]
