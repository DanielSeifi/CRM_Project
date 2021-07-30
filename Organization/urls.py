from django.urls import path
from .views import create_organ,create_organ_product

namespace='Organization'
urlpatterns = [
    path('',create_organ.as_view(),name="CreateOrgan"),
    path('organ_product/',create_organ_product.as_view(),name="CreateOrganProduct"),
]
