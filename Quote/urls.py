from django.urls import path
from .views import craete_quote
app_name='Quote'
urlpatterns = [
    path('', craete_quote.as_view(), name='CreateQuote'),
]
