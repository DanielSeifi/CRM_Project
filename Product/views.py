from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product

# Create your views here.
from django.views.generic import ListView


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'ProductList.html'
    paginate_by = 4
