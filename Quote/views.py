from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from Organization.models import Organization
from Quote.forms import QuoteItemCreateFormSet
from .models import QuoteItem


class craete_quote(LoginRequiredMixin, CreateView):
    template_name = "CreateQuote.html"

    def get_context_data(self, **kwargs):
        formset = QuoteItemCreateFormSet(queryset=QuoteItem.objects.none())
        organizations = Organization.objects.filter(user_creator=self.request.user)
        return {'formset': formset, 'organizations': organizations}