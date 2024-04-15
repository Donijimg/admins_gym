from django.db import models


class Admin(models.Model):
    identificacion_propietario = models.CharField(max_length=10, blank=True, null=True)  
    documento = models.CharField(max_length=10, blank=True, null=True) 
    nombre_admin = models.CharField(max_length=15, blank=False, null=False)
    apellido_admin = models.CharField(max_length=15, blank=False, null=False)
    contrasena_admin = models.CharField(max_length=10, blank=False, null=False)
    correo = models.EmailField(max_length=20, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)  

    def __str__(self):
        return f"{self.identificacion_propietario} {self.documento}"

class Coach(models.Model):
    documento = models.CharField(max_length=10, blank=True, null=True) 
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    ESPACIALIZACION_CHOICES=(
            ('', 'Seleccione su especialización'), 
            ('Fitness', 'Fitness'),
            ('Pilates', 'Pilates'),
            ('Rehabilitación física', 'Rehabilitación física'),
            ('Plan para mayores', 'Plan para mayores'),
            ('Yoga', 'Yoga'),
            ('Gimnasia', 'Gimnasia'))
    HORA_CHOICES = (
            ('', 'Seleccione un horario'),
            ('Mañana (5:00am - 8:00am)', 'Mañana (5:00am - 8:00am)'),
            ('Tarde (2:00pm - 5:00pm)', 'Tarde (2:00pm - 5:00pm)'),
            ('Noche (6:00pm - 9:00pm)', 'Noche (6:00pm - 9:00pm)'),
            ('Madrugada (10:00pm - 1:00am)', 'Madrugada (10:00pm - 1:00am)'))
    especializacion = models.CharField(max_length=30, choices=ESPACIALIZACION_CHOICES, blank=False)
    horarios = models.CharField(max_length=30, choices=HORA_CHOICES, blank=False)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    correo = models.EmailField(max_length=20, blank=False, null=False)
    direccion = models.CharField(max_length=10, blank=False, null=False)
    experiencia = models.IntegerField(blank=True, null=True)
    contrasena = models.CharField(max_length=10, blank=False, null=False)   
    ficha_de_ingreso = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class User(models.Model):
    documento = models.CharField(max_length=10, blank=True, null=True) 
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    contrasena=models.CharField(max_length=10, blank=False, null=False)
    entrenador = models.ForeignKey(Coach, on_delete=models.CASCADE, blank=True, null=True)


class Inscripcion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    inscripcion = models.CharField(max_length=20, blank=True, null=True)
    entrenador = models.ForeignKey(Coach, on_delete=models.CASCADE, blank=True, null=True)
    horarios = models.CharField(max_length=20, blank=True, null=True)


class historial(models.Model):
    pago_membresia = models.BooleanField(default=False, null=True)
    entrenador = models.ForeignKey(Coach, on_delete=models.CASCADE)

    
    
