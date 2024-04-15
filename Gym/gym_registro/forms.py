# forms.py
from django import forms
from .models import Admin, Coach,User,Inscripcion

class InscripcionUser(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['inscripcion', 'entrenador', 'horarios']

class SignupAdmin(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['identificacion_propietario', 'documento', 'nombre_admin', 'apellido_admin', 'contrasena_admin', 'correo', 'telefono', 'direccion']
        labels = {
            'identificacion_propietario': 'Identificación Propietario:',
            'documento': 'Documento:',
            'nombre_admin': 'Nombre:',
            'apellido_admin': 'Apellido:',
            'contrasena_admin': 'Contraseña:',
            'correo': 'Correo Electrónico:',
            'telefono': 'Teléfono:',
            'direccion': 'Dirección:'
        }
        widgets = {
            'identificacion_propietario': forms.TextInput(attrs={'class': 'input_uni'}),
            'documento': forms.TextInput(attrs={'class': 'input_uni'}),
            'nombre_admin': forms.TextInput(attrs={'class': 'input_uni'}),
            'apellido_admin': forms.TextInput(attrs={'class': 'input_uni'}),
            'contrasena_admin': forms.PasswordInput(attrs={'class': 'input_uni'}),
            'correo': forms.EmailInput(attrs={'class': 'input_uni'}),
            'telefono': forms.TextInput(attrs={'class': 'input_uni'}),
            'direccion': forms.TextInput(attrs={'class': 'input_uni'}),
        }


class SignupCoach(forms.ModelForm):
    especializacion = forms.ChoiceField(
        label="Especialización:",
        choices=(
            ('', 'Seleccione su especialización'),  
            ('Fitness', 'Fitness'),
            ('Pilates', 'Pilates'),
            ('Rehabilitación física', 'Rehabilitación física'),
            ('Plan para mayores', 'Plan para mayores'),
            ('Yoga', 'Yoga'),
            ('Gimnasia', 'Gimnasia')
        ),
        widget=forms.Select(attrs={'class':'input_uni'}),
        required=True
    )

    horarios = forms.ChoiceField(
        label="Horarios:",
        choices=(
            ('', 'Seleccione un horario'),  
            ('Mañana (5:00am - 8:00am)', 'Mañana (5:00am - 8:00am)'),
            ('Tarde (2:00pm - 5:00pm)', 'Tarde (2:00pm - 5:00pm)'),
            ('Noche (6:00pm - 9:00pm)', 'Noche (6:00pm - 9:00pm)'),
            ('Madrugada (10:00pm - 1:00am)', 'Madrugada (10:00pm - 1:00am)')
        ),
        widget=forms.Select(attrs={'class':'input_uni'}),
        required=True
    )

    genero = forms.ChoiceField(
        label="Género:",
        choices=(
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('Otro', 'Otro'),
        ),
        widget=forms.Select(attrs={'class':'input_uni'}),
        required=True
    )

    class Meta:
        model = Coach
        fields = ['documento', 'nombre', 'apellido', 'edad', 'genero', 'telefono', 'correo', 'direccion', 'experiencia', 'contrasena', 'ficha_de_ingreso', 'especializacion', 'horarios']
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'edad': 'Edad:',
            'genero': 'Género:',
            'telefono': 'Teléfono:',
            'correo': 'Correo Electrónico:',
            'direccion': 'Dirección:',
            'experiencia': 'Experiencia:',
            'contrasena': 'Contraseña:',
            'ficha_de_ingreso': 'Ficha de Entrenador:',
            'especializacion': 'Especialización:',
            'horarios': 'Horarios:'
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'input_uni', 'placeholder': 'Edad'}),
            'genero': forms.Select(attrs={'class': 'input_uni'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder': 'Teléfono'}),
            'correo': forms.EmailInput(attrs={'class':'input_uni', 'placeholder': 'E-mail'}),
            'direccion': forms.TextInput(attrs={'class':'input_uni', 'placeholder': 'Dirección'}),
            'experiencia': forms.NumberInput(attrs={'class': 'input_uni', 'placeholder': 'Experiencia'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder': 'Contraseña'}),
            'ficha_de_ingreso': forms.TextInput(attrs={'class':'input_uni', 'placeholder': 'Ficha de Entrenador'}),
            'especializacion': forms.Select(attrs={'class': 'input_uni'}),
            'horarios': forms.Select(attrs={'class': 'input_uni'})
        }


class SignupUser(forms.ModelForm):
    class Meta:
        model = User
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