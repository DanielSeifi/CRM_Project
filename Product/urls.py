from django.urls import path
from .views import CreateProduct,ProductList
namespace='Product'
urlpatterns = [
    path('', CreateProduct.as_view(), name='CreateProduct',),
    path('productlist/', ProductList.as_view(), name='ProductList',),
]
