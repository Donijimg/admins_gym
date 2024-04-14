# forms.py
from django import forms
from .models import Admin, Coach, UserRegistration

class SignupAdmin(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['identificacion_propietario', 'documento', 'nombre_admin', 'apellido_admin', 'telefono', 'direccion', 'correo', 'contrasena_admin']
        labels = {
            'identificacion_propietario': 'Identificación del Propietario:',
            'documento': 'Documento:',
            'nombre_admin': 'Nombre:',
            'apellido_admin': 'Apellido:',
            'telefono': 'Teléfono:',
            'direccion': 'Dirección:',
            'correo': 'Correo Electrónico:',
            'contrasena_admin': 'Contraseña de Administrador:'
        }
        widgets = {
            'identificacion_propietario': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Identificación del Propietario'}),
            'documento': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Número de Documento'}),
            'nombre_admin': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Nombre de Administrador'}),
            'apellido_admin': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Apellido'}),
            'telefono': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': '+(57) --- --- ----'}),
            'direccion': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Dirección'}),
            'correo': forms.EmailInput(attrs={'class': 'input_uni', 'placeholder': 'Correo Electrónico'}),
            'contrasena_admin': forms.PasswordInput(attrs={'class': 'input_uni', 'placeholder': 'Contraseña de Administrador'}),
        }

class SignupCoach(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['documento', 'nombre', 'apellido', 'direccion', 'edad', 'telefono', 'correo', 'genero', 'contrasena', 'ficha_de_ingreso', 'experiencia', 'especializacion', 'horarios']
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'direccion': 'Dirección:',
            'edad': 'Edad:',
            'telefono': 'Teléfono:',
            'correo': 'Correo Electrónico:',
            'genero': 'Género:',
            'contrasena': 'Contraseña:',
            'ficha_de_ingreso': 'Ficha de Entrenador:',
            'experiencia': 'Experiencia:',
            'especializacion': 'Especialización:',
            'horarios': 'Horarios:',
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Numero de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'direccion': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Dirección'}),
            'edad': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Edad'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'+(57) --- --- ----'}),
            'correo': forms.EmailInput(attrs={'class':'input_uni', 'placeholder':'E-mail'}),
            'genero': forms.RadioSelect(attrs={'class': 'input_radio'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
            'ficha_de_ingreso': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Ficha de Entrenador'}),
            'experiencia': forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Experiencia'}),
            'especializacion': forms.Select(attrs={'class':'input_uni'}),
            'horarios': forms.Select(attrs={'class':'input_uni'}),
        }

class SignupUser(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['documento', 'nombre', 'apellido', 'telefono', 'edad', 'contrasena', 'genero']
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'telefono': 'Número de teléfono:',
            'edad': 'Edad:',
            'contrasena': 'Contraseña:',
            'genero': 'Género:',
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de teléfono'}),
            'edad': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Edad'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
            'genero': forms.RadioSelect(attrs={'class':'input_radio'}),
        }
