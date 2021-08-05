from django.urls import path
from .views import craete_quote,quote_list
app_name='Quote'
urlpatterns = [
    path('', craete_quote.as_view(), name='CreateQuote'),
    path('quotelist/', quote_list.as_view(), name='QuoteList'),
]
