from django.urls import path
from . import views

urlpatterns = [
    path("", views.realtor_list, name="realtor_list"),
]
