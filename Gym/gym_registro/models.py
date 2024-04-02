from django.db import models

class Entrenador(models.Model):
    ficha_de_ingreso = models.IntegerField(blank=False, null=False)
    documento = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=75, blank=False, null=False)
    direccion = models.TextField(null=False)
    anos_de_experiencia = models.IntegerField(blank=False, null=False)
    conocimiento = models.TextField(null=False)
    horario_de_entrada = models.TimeField()
    horario_de_salida = models.TimeField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class InscripcionCliente(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    rutina_actual = models.TextField(null=False)
    lesiones = models.TextField(null=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=4, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    objetivos = models.TextField(null=False)
    inscripcion = models.CharField(max_length=15, blank=False, null=False)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class RutinaCliente(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)  
    rutina_diaria = models.TextField(null=False)
    complicaciones = models.TextField(null=False)
    rendimiento = models.TextField(null=False)
    dieta = models.TextField(null=False)
    faltas = models.IntegerField(blank=False, null=False)
    pago_membresia = models.BooleanField(default=False)
    avances = models.TextField(null=False)
    horario_asignado = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
