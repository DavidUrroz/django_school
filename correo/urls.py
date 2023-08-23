from django.urls import path
from . import views


urlpatterns = [
    path("correo", views.Correo.as_view(), name="correo")
]