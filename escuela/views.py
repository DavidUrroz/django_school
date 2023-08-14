# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from .models import Escuela, Estudiante, Maestro
from .serializers import EscuelaSerializer, EstudianteSerializer, MaestroSerializer
# Create your views here.

class EscuelaViewset(ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstudianteViewset(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MaestroViewset(ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer