from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
 
router.register('escuelas', views.EscuelaViewset)
router.register('estudiantes', views.EstudianteViewset)
router.register('maestros', views.MaestroViewset)

urlpatterns = [
]

urlpatterns += router.urls