from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models, forms

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView


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
    model = models.Organization
    template_name = 'OrganList.html'
    paginate_by = 4


class organ_detail(LoginRequiredMixin, DetailView):
    model = models.Organization
    template_name = 'OrganDetail.html'

    def get_queryset(self):
        organization = models.Organization.objects.filter(pk=self.kwargs['pk'], user_creator=self.request.user)
        return organization


class create_follow_up(LoginRequiredMixin, CreateView):
    pass
