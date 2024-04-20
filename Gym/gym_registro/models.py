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
    
    TURNO_CHOICES=(
        (1, '-----'),
        (2, 'Noche'),
        (3, 'Dia'),
    )
    
    ESPECIALIZACIONES_CHOICES = (
        (1, '-------'),
        (2, 'Fitness'),
        (3, 'Pilates'),
        (4, 'Rehabilitacion fisica'),
        (5, 'Plan para mayores'),
        (6, 'Yoga'),
        (7, 'Gimnasia')
        # Agrega más especializaciones según sea necesario
    )
    turno = models.IntegerField(choices=TURNO_CHOICES, blank=True, null=True)
    typo_id = models.IntegerField(choices=ESPECIALIZACIONES_CHOICES, blank=True, null=True)
    usuarios = models.ManyToManyField('User', related_name='coaches', blank=True)  # Agrega blank=True
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='coaches', blank=True, null=True)
    GENE_CHOICES=(
        (1, '---------'),
        (2, 'Masculino'),
        (3, 'Femenino'),
        (4, 'Otro'),
    )
    genero = models.IntegerField(choices=GENE_CHOICES, blank=True, null=True)

class User(models.Model):
    documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    contrasena = models.CharField(max_length=128, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)   
    GENE_CHOICES=(
        (1, 'Masculino'),
        (2, 'Femenino'),
    )
    genero = models.IntegerField(choices=GENE_CHOICES, blank=True, null=True)

class SolicitudesCliente(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    estatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    objetivos = models.TextField(blank=True)
    correo = models.EmailField(max_length=100, blank=False, null=False)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='solicitudes_clientes', blank=True, null=True)

