from django import forms
from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            'product_name',
            'price',
            'is_tax',
            'pdf_file',
            'image_file',
            'feature',
            'company_rel_organ',
        ]
