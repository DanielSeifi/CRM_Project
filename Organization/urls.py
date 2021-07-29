from django.urls import path
from .views import create_organ

namespace='Organization'
urlpatterns = [
    path('',create_organ.as_view(),name="CreateOrgan"),
]
