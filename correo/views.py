from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from escuela.models import Estudiante
from demoEscuela.settings import EMAIL_HOST_USER
# Create your views here.


class Correo(APIView):

    def post(self, request):
        estudiante = request.data.get("estudiante", None)

        if estudiante:

            # try:
                estudiante = Estudiante.objects.get(pk=estudiante)
                mensaje = f"Se ha creado un estudiante en el sistema, Nombre: {estudiante.name} {estudiante.last_name}"
                send_mail(
                    "Confirmación de ingreso",
                    mensaje,
                    EMAIL_HOST_USER,
                    [EMAIL_HOST_USER],
                    fail_silently=False
                )
                # return Response({"mensaje": "Se ha enviado el correo"})
            # except Exception as e:

                # return Response({"error": str(e)})
        else:
            return Response({"mensaje": "No se ha enviado el estudiante"})