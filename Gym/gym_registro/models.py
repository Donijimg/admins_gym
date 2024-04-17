from django.db import models


class Admin(models.Model):
    identificacion_propietario = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre_admin = models.CharField(max_length=50, blank=False, null=False)
    apellido_admin = models.CharField(max_length=50, blank=False, null=False)
    contrasena_admin = models.CharField(max_length=128, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)

    

class Coach(models.Model):
    documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=False, null=False)
    experiencia = models.IntegerField(blank=True, null=True)
    contrasena = models.CharField(max_length=128, blank=False, null=False)
    ficha_de_ingreso = models.CharField(max_length=10, blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)
    horarios = models.CharField(max_length=30, blank=False, null=False)
    ESPECIALIZACIONES_CHOICES = (
    (1, 'Fitness'),
    (2, 'Pilates'),
    (3, 'Rehabilitacion fisica'),
    (4, 'Plan para mayores'),
    (5, 'Yoga'),
    (6, 'Gimnasia')

    # Agrega más especializaciones según sea necesario
)
    typo_id = models.IntegerField(choices=ESPECIALIZACIONES_CHOICES, blank=True, null=True)

class User(models.Model):
    documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    contrasena = models.CharField(max_length=128, blank=False, null=False)
    # entrenador = models.ManyToManyField(Coach, related_name='entrenadores', blank=True)

class Inscripcion(models.Model):
    usuario = models.ManyToManyField(User, related_name='inscripciones', blank=True)
    entrenador = models.ManyToManyField(Coach, related_name='inscripciones', blank=True)



