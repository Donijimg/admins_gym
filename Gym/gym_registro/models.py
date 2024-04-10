from django.db import models

class Admin(models.Model):

    identificacion_propietario = models.IntegerField(max_length=9999999, blank=False, null=False)
    documento = models.IntegerField(max_length=10, blank=False, null=False)
    nombre_admin = models.CharField(max_length=40, blank=False, null=False, unique=True)
    apellido_admin = models.CharField(max_length=40, blank=False, null=False)
    contrasena_admin = models.CharField(max_length=40, blank=False, null=False)
    correo = models.EmailField(max_length=75, blank=False, null=False)
    telefono = models.CharField(max_length=14, blank=False, null=False)
    direccion = models.CharField(max_length=75, blank=False, null=False)
    redes_sociales = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Coach(models.Model):
    documento = models.IntegerField(max_length=9999999999, blank=False, null=False)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    edad= models.IntegerField(max_length=90, blank=False, null=False)
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=False, null=False)
    telefono = models.CharField(max_length=14, blank=True, null=True)
    correo = models.EmailField(max_length=75, blank=False, null=False)
    direccion = models.CharField(max_length=75, blank=False, null=False)
    experiencia =  models.IntegerField(max_length=2, blank=True, null=True)
    especializacion = models.CharField(max_length=40, blank=True, null=True)
    horarios = models.CharField(max_length=20, blank=True, null=True)
    contrasena = models.CharField(max_length=40, blank=False, null=False)   
    ficha_de_ingreso = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class UserRegistration(models.Model):
    documento= models.IntegerField(max_length=9999999999, blank=False, null=False)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    apellido = models.CharField(max_length=40, blank=False, null=False)
    edad = models.IntegerField(max_length=90,blank=False, null=False)
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=False, null=False)
    telefono = models.CharField(max_length=14, blank=False, null=False)
    contrasena=models.CharField(max_length=40, blank=False, null=False)
    #vista inscrisiones
    inscripcion = models.BooleanField(default=False)
    entrenador = models.ForeignKey(Coach, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#vista del entrenador para registrear seciones de entrenamiento
class ClientRoutine(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    estatura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    rutina = models.TextField(null=False)
    dieta = models.TextField(null=False)
    pago_membresia = models.BooleanField(default=False ,null=True)
    entrenador = models.ForeignKey(Coach, on_delete=models.CASCADE)
    horarios = models.CharField(max_length=20, blank=True, null=True)



    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Diets(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

