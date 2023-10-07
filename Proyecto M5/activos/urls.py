from os import name
from unittest.mock import patch
from django.urls import path
from . import views

urlpatterns = [
    path("contact/<str:name>", views.contact, name="index"),
    path("", views.index, name="index"),
    path("grupos/", views.grupos, name="grupos"),
    path("activos/", views.activos, name="activos"),
]