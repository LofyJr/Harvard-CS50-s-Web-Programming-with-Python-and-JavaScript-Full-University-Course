from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("Lofy", views.Lofy, name="Lofy"),
    path("Junior", views.Junior, name="Junior")
]