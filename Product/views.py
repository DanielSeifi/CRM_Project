from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product

# Create your views here.
from django.views.generic import CreateView


class CreateProduct(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'CreateProduct.html'
    model = Product
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user_creator = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)
