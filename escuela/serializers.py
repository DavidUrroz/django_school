from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    RelatedField,
)
from .models import Escuela, Estudiante, Maestro, Salon


class EscuelaSerializer(ModelSerializer):
    # El ModelSerializer crea automaticamente un serializer ligados a los campos
    # que definimos en nuestro modelo de datos.

    # Automáticamente nos das los métodos .create() y .update() para trabajar
    # sobre la base de datos.

    class Meta:
        model = Escuela
        # fields = ["id", "name", "location", "email", "contact_number"]

        fields = "__all__"

        # exclude = ["email"]

        # read_only_fields = ["contact_number"]

        # Al dejar fuera un campo del serializer que tenemos en el modelo ya sea con fields o
        # exclude, ese campo se toma como si tuviera la propiedad blank=True en nuestro su
        # esquema.

        # Podemos espeficificar campos que queramos que sean de solo lectura con el siguiente
        # patrón

        extra_kwargs = {"location": {"write_only": True}}


class EstudianteSerializer(ModelSerializer):
    # Todas las relaciones directas a un padre pueden ser accedidas con PrimaryKeyRelatedField,
    # las relaciones inversas para mostrar a un hijo no están incluidas por default y tienen que
    # ser incluídas explícitamente.

    # Podemos especificar los datos que queramos obtener del padre con el parámetro source y utilizando
    # la notación del punto para obtener los atributos del padre.

    school_name = PrimaryKeyRelatedField(source="school.name", read_only=True)

    class Meta:
        model = Estudiante
        fields = "__all__"


class MaestroSerializer(ModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"


class SalonSerializer(ModelSerializer):
    class Meta:
        model = Salon
        fields = "__all__"