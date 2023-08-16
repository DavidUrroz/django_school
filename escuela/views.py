# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Escuela, Estudiante, Maestro
from .serializers import EscuelaSerializer, EstudianteSerializer, MaestroSerializer
# Create your views here.

class EscuelaViewset(ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer




class EstudianteViewset(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def list(self, request):
        queryset = Estudiante.objects.all()
        school = request.GET.get("school", None)

        if school is not None:
            return Response(
                self.serializer_class(queryset.filter(school=school), many=True).data)
        
        else:
            return Response(self.serializer_class(queryset, many=True).data)


class MaestroViewset(ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer



def suma(a, b):
    return a + b

resta = suma

suma(1, 2)

resta(1, 2) # 3

a = print

a("Hello world")