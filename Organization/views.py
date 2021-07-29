from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from . import models,forms

# Create your views here.
from django.views.generic import CreateView


class create_organ(LoginRequiredMixin,CreateView):
    model = models.Organization
    template_name = 'CreateOrgan.html'
    form_class = forms.OrganForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        form.instance.user_creator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)
