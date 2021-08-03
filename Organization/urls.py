from django.urls import path
from .views import create_organ,organs_list

app_name='Organization'
urlpatterns = [
    path('',create_organ.as_view(),name="CreateOrgan"),
    path('organslist/',organs_list.as_view(),name="OrgansList"),
]
