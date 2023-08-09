from rest_framework.serializers import ModelSerializer
from .models import Escuela, Estudiante, Maestro


class EscuelaSerializer(ModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

        
class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"


class MaestroSerializer(ModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"