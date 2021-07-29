from django import forms
from . import models


class OrganForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = [
            'state',
            'name',
            'phone',
            'workers_qty',
            'organ_product',
            'full_name_owner',
            'phone_owner',
            'email_owner',
        ]