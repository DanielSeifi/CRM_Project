from django.urls import path
from .views import create_organ,organs_list,create_follow_up

app_name='Organization'
urlpatterns = [
    path('',create_organ.as_view(),name="CreateOrgan"),
    path('organslist/',organs_list.as_view(),name="OrgansList"),
    path('createfollowup/<int:pk>',create_follow_up.as_view(),name="CreateFollowUp"),
]
