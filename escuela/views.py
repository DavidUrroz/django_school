# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Escuela, Estudiante, Maestro
from .serializers import EscuelaSerializer, EstudianteSerializer, MaestroSerializer
# Create your views here.

class EscuelaViewset(ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer


class EstudianteViewset(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class MaestroViewset(ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer