from django.db import models

class AdminOficial(models.Model):
#este tabla y login y registro solo sera accedido po url para seguridad de que el usuario no autorizado no acceda
    identificacion_propietario = models.CharField(max_length=7, blank=False, null=False)
    documento = models.CharField(max_length=10, blank=False, null=False)
    nombre_admin = models.CharField(max_length=15, blank=False, null=False, unique=True)
    apellido_admin = models.CharField(max_length=30, blank=False, null=False)
    contrasena_admin = models.CharField(max_length=40, blank=False, null=False)
    correo = models.EmailField(max_length=75, blank=False, null=False)
    telefono = models.CharField(max_length=14, blank=False, null=False)
    direccion = models.CharField(max_length=75, blank=False, null=False)
    redes_sociales = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entrenador(models.Model):
# para cuando "signup entrenador"=registres el entrenador
#datos por llenar
    documento = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    fecha_nacimiento = models.DateField()
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    correo = models.EmailField(max_length=75, blank=False, null=False)
    direccion = models.CharField(max_length=75, blank=False, null=False)
    experiencia = models.IntegerField(blank=False, null=False)
    conocimiento = models.TextField(null=False)
    # foto_perfil = models.ImageField(upload_to='foto_perfil/', blank=True, null=True)
    horario_de_entrada = models.TimeField()#esto sera un opcion
    horario_de_salida = models.TimeField()#esto sera un opcion
# para registrar y logear
    nombre_usuario = models.CharField(max_length=15, blank=False, null=False, unique=True)
    contrasena = models.CharField(max_length=40, blank=False, null=False)
#una ves iniciada seccion puedes agregar datos adicionales
    redes_sociales = models.URLField(max_length=200, blank=True, null=True)    
#se generara al registrarse una ficha al logearse se te sera pedida
    ficha_de_ingreso = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#tabla para que los usuarios o cliente puedan logearse he inscribirse
class InscripcionCliente(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido = models.CharField(max_length=15, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    genero = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    rutina_actual = models.TextField(null=False)
    historial_lesiones = models.TextField(null=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=4, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    objetivos = models.TextField(null=False)
    inscripcion = models.BooleanField(default=False)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#esta tabla solo la manejan los entrenadores y consulta el admin  los 
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
    pago_membresia =models.BooleanField(default=False)
    avances = models.TextField(null=False)
    horario_asignado = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
