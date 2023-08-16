from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter(trailing_slash=False)

# router.register("escuelas", views.EscuelaViewset)
# router.register("estudiantes", views.EstudianteViewset)
# router.register("maestros", views.MaestroViewset)

urlpatterns = [
    path(
        "escuelas",
        views.EscuelaViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "escuelas/<int:pk>",
        views.EscuelaViewset.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]

# urlpatterns += router.urls
