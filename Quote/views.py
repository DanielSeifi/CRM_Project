from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from Organization.models import Organization
from .forms import QuoteItemCreateFormSet
from .models import QuoteItem,Quote


class craete_quote(LoginRequiredMixin, CreateView):
    template_name = "CreateQuote.html"

    def get_context_data(self, **kwargs):
        formset = QuoteItemCreateFormSet(queryset=QuoteItem.objects.none())
        organizations = Organization.objects.filter(user_creator=self.request.user)
        return {'formset': formset, 'organizations': organizations}

    def post(self, *args, **kwargs):
        formset = QuoteItemCreateFormSet(data=self.request.POST)
        if formset.is_valid():
            organization = get_object_or_404(Organization, pk=self.request.POST['organization'],
                                             user_creator=self.request.user)
            quote = Quote.objects.create(user_creator=self.request.user, organ=organization)
            for form in formset:
                form.instance.quote = quote
                form.save()
            messages.success(self.request, "ثبت شد")
            return redirect(reverse_lazy("Organization:OrgansList"))

class quote_list(LoginRequiredMixin, ListView):
    model = Quote
    template_name = 'QuoteList.html'
    paginate_by = 4