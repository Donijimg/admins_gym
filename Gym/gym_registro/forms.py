from django import forms
from .models import Admin, Coach, User, SolicitudesCliente

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input_uni'
            field.widget.attrs['placeholder'] = field.label

class SolicitudesClienteForm(BaseForm):
    class Meta:
        model = SolicitudesCliente
        fields = ['peso', 'estatura', 'objetivos', 'correo']
        labels = {
            'peso': 'Peso:',
            'estatura': 'Estatura:',
            'correo': 'Correo',
            'objetivos': 'Objetivos'
        }
        widgets = {
            'peso': forms.TextInput(),
            'estatura': forms.TextInput(),
            'objetivos': forms.Textarea(),
            'correo': forms.EmailInput(),
        }

class SignupAdmin(BaseForm):
    class Meta:
        model = Admin
        fields = '__all__'
        labels = {
            'identificacion_propietario': 'Identificación Propietario:',
            'documento': 'Documento:',
            'nombre_admin': 'Nombre:',
            'apellido_admin': 'Apellido:',
            'contrasena_admin': 'Contraseña:',
            'correo': 'Correo Electrónico:'
        }
        widgets = {
            'identificacion_propietario': forms.TextInput(),
            'documento': forms.TextInput(),
            'nombre_admin': forms.TextInput(),
            'apellido_admin': forms.TextInput(),
            'contrasena_admin': forms.PasswordInput(),
            'correo': forms.EmailInput(),
        }

class SignupCoach(BaseForm):
    typo_id = forms.ChoiceField(choices=Coach.ESPECIALIZACIONES_CHOICES, label='Especialización')
    turno = forms.ChoiceField(choices=Coach.TURNO_CHOICES, label='Turno')
    genero = forms.ChoiceField(choices=Coach.GENE_CHOICES, label='Género')  # Agregar campo genero

    class Meta:
        model = Coach
        fields = '__all__'
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'edad': 'Edad:',
            'telefono': 'Teléfono:',
            'correo': 'Correo Electrónico:',
            'experiencia': 'Experiencia:',
            'contrasena': 'Contraseña:',
            'ficha_de_ingreso': 'Ficha de Entrenador:',
            'horarios': 'Horarios:',
            'typo_id': 'Especialización:',
            'turno': 'Turno:',  # Agregar etiqueta para el campo turno
            'genero': 'Género:',  # Agregar etiqueta para el campo genero
        }
        widgets = {
            'documento': forms.TextInput(),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'edad': forms.NumberInput(),
            'telefono': forms.TextInput(),
            'correo': forms.EmailInput(),
            'experiencia': forms.NumberInput(),
            'contrasena': forms.PasswordInput(),
            'ficha_de_ingreso': forms.TextInput(),
            'horarios': forms.TextInput(),
        }

class SignupUser(BaseForm):
    genero = forms.ChoiceField(choices=User.GENE_CHOICES, label='Género')  # Agregar campo genero

    class Meta:
        model = User
        exclude = ['admin']
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'telefono': 'Número de teléfono:',
            'edad': 'Edad:',
            'contrasena': 'Contraseña:',
            'correo': 'Correo:',
            'genero': 'Género:',  # Agregar etiqueta para el campo genero
        }
        widgets = {
            'documento': forms.TextInput(),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'telefono': forms.TextInput(),
            'edad': forms.TextInput(),
            'contrasena': forms.PasswordInput(),
            'correo': forms.EmailInput(),
        }




