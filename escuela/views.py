# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions


# from .permissions import IsOwnerOrReadOnly
from .models import Escuela, Estudiante, Maestro
from .serializers import EscuelaSerializer, EstudianteSerializer, MaestroSerializer

# Create your views here.


class EscuelaViewset(ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

    def list(self, request):
        name = request.GET.get("name", None)
        email = request.GET.get("email", None)

        if name and email:
            return Response(
                self.serializer_class(
                    self.queryset.filter(name__icontains=name, email__icontains=email),
                    many=True,
                ).data
            )

        elif name:
            return Response(
                self.serializer_class(
                    self.queryset.filter(name__icontains=name),
                    many=True,
                ).data
            )

        elif email:
            return Response(
                self.serializer_class(
                    self.queryset.filter(email__icontains=email), many=True
                ).data
            )

        else:
            return Response(self.serializer_class(self.queryset, many=True).data)


class EstudianteViewset(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MaestroViewset(ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer
