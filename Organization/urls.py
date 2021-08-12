from django.urls import path
from .views import create_organ,organs_list,organ_detail,organ_update,show_follow_up,create_follow_up

app_name='Organization'
urlpatterns = [
    path('',create_organ.as_view(),name="CreateOrgan"),
    path('organslist/',organs_list.as_view(),name="OrgansList"),
    path('organdetail/<int:pk>',organ_detail.as_view(),name="OrganDetail"),
    path('organupdate/<int:pk>',organ_update.as_view(),name="OrganUpdate"),
    # path('showfollowup/<int:pk>', show_follow_up.as_view(), name="ShowFollowUp"),
    path('createfollowup/<int:pk>', create_follow_up.as_view(), name="CreateFollowUp"),
]
