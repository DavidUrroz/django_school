from django.db import models

# Create your models here.

class Escuela(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Salon(models.Model):

    codigo = models.TextField(default="")
    desks_quant = models.SmallIntegerField()
    fans_quant = models.SmallIntegerField(blank=True, default=0)
    acrylic_board = models.BooleanField()

    def __str__(self):
        return self.codigo


class Estudiante(models.Model):

    grades = [
        ("1°", "Primer grado"),
        ("2°", "Segundo grado"),
        ("3°", "Tercer grado"),
        ("4°", "Cuarto grado"),
        ("5°", "Quinto grado"),
        ("6°", "Sexto grado"),
    ]

    school = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_grade = models.CharField(max_length=20, choices=grades)
    domicile = models.TextField()

    def __str__(self):
        return self.name

class Maestro(models.Model):

    school = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=60)
    years_of_experience = models.SmallIntegerField()
    on_duty = models.BooleanField()


class Registros(models.Model):

    nombre = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="static/uploads/")