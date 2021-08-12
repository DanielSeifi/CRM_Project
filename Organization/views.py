from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models, forms, serializers

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, FormView


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


class organ_update(LoginRequiredMixin, UpdateView):
    model = models.Organization
    template_name = 'EditOrgan.html'
    form_class = forms.OrganForm

    def get_queryset(self):
        organization = models.Organization.objects.filter(pk=self.kwargs['pk'], user_creator=self.request.user)
        return organization

    def get_success_url(self):
        return reverse_lazy('Organization:OrganDetail', kwargs={'pk': self.object.pk})


class show_follow_up(LoginRequiredMixin, CreateView):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class create_follow_up(LoginRequiredMixin, CreateView):
    model = models.FollowUp
    fields = [
        'description'
    ]
    template_name = 'CreateFollowUp.html'

    def form_invalid(self, form):
        return JsonResponse(data={
            'success': 'False',
        }, status=400)

    def form_valid(self, form):
        form.save(commit=False).user_creator = self.request.user
        form.save(commit=False).organization = models.Organization.objects.get(pk=self.kwargs['pk'])
        form.save()
        return JsonResponse(data={
            'success': 'True',
        }, status=200)

    def get_context_data(self, **kwargs):
        context = {
            'organization': models.Organization.objects.get(pk=self.kwargs['pk']),
        }
        return context


class OrganizationViewSetAPI(ModelViewSet):
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = models.Organization.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
