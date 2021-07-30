from django.urls import path
from .views import CreateProduct
namespace='Product'
urlpatterns = [
    path('', CreateProduct.as_view(), name='CreateProduct',)
]
