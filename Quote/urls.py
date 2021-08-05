from django.urls import path
from .views import craete_quote,quote_list,send_email
app_name='Quote'
urlpatterns = [
    path('', craete_quote.as_view(), name='CreateQuote'),
    path('quotelist/', quote_list.as_view(), name='QuoteList'),
    path('sendemail/<int:pk>', send_email, name='SendEmail'),
]
