from django.db import models

# Create your models here.

class Contacto(models.Model):

    nombre = models.CharField(max_length=80) 
    edad = models.SmallIntegerField(blank=True)
    email = models.EmailField()
    proveedor = models.ForeignKey("Proveedor", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):

    nombre = models.CharField(max_length=80)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre