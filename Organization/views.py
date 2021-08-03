from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models, forms

# Create your views here.
from django.views.generic import CreateView, ListView


class create_organ(LoginRequiredMixin, CreateView):
    model = models.Organization
    template_name = 'CreateOrgan.html'
    form_class = forms.OrganForm
    success_url = reverse_lazy("Organization:OrgansList")

    def form_valid(self, form):
        form.instance.user_creator = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


class organs_list(LoginRequiredMixin, ListView):
    pass
