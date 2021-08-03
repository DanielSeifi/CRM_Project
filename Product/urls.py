from django.urls import path
from .views import ProductList
app_name='Product'
urlpatterns = [
    path('productlist/', ProductList.as_view(), name='ProductList',),
]
