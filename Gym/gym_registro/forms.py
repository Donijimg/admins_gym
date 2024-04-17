# forms.py
from django import forms
from .models import Admin, Coach, User,SolicitudesCliente
from django.core.mail import send_mail


class SolicitudesClienteForm(forms.ModelForm):
    class Meta:
        model = SolicitudesCliente
        fields = [ 'peso', 'estatura', 'objetivos','correo']
        labels = {
 
            'peso': 'Peso:',
            'estatura': 'Estatura:',
            'correo': 'Correo',
            'objetivos': 'objetivos'
        }
        
        widgets = {
            'peso': forms.TextInput(attrs={'class': 'input_uni'}),
            'estatura': forms.TextInput(attrs={'class': 'input_uni'}),
            'objetivos': forms.Textarea(attrs={'class': 'input_uni'}),
            'correo': forms.EmailInput(attrs={'class': 'input_uni'}),
         }




class SignupAdmin(forms.ModelForm):
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
            'identificacion_propietario': forms.TextInput(attrs={'class': 'input_uni'}),
            'documento': forms.TextInput(attrs={'class': 'input_uni'}),
            'nombre_admin': forms.TextInput(attrs={'class': 'input_uni'}),
            'apellido_admin': forms.TextInput(attrs={'class': 'input_uni'}),
            'contrasena_admin': forms.PasswordInput(attrs={'class': 'input_uni'}),
            'correo': forms.EmailInput(attrs={'class': 'input_uni'}),
        }



class SignupCoach(forms.ModelForm):
    # Define el campo typo_id como ChoiceField
    typo_id = forms.ChoiceField(choices=Coach.ESPECIALIZACIONES_CHOICES, label='Especialización', widget=forms.Select(attrs={'class': 'input_uni'}))

    class Meta:
        model = Coach
        fields = '__all__'
        labels = {
            'documento': 'Documento:',
            'nombre': 'Nombre:',
            'apellido': 'Apellido:',
            'edad': 'Edad:',
            'genero': 'Género:',
            'telefono': 'Teléfono:',
            'correo': 'Correo Electrónico:',
            'experiencia': 'Experiencia:',
            'contrasena': 'Contraseña:',
            'ficha_de_ingreso': 'Ficha de Entrenador:',
            'horarios': 'Horarios:',
            'typo_id': 'Especialización:',  # Cambiar type_id a typo_id
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'input_uni', 'placeholder': 'Edad'}),
            'genero': forms.TextInput(attrs={'class': 'input_uni'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder': 'Teléfono'}),
            'correo': forms.EmailInput(attrs={'class':'input_uni', 'placeholder': 'E-mail'}),
            'experiencia': forms.NumberInput(attrs={'class': 'input_uni', 'placeholder': 'Experiencia'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder': 'Contraseña'}),
            'ficha_de_ingreso': forms.TextInput(attrs={'class':'input_uni', 'placeholder': 'Ficha de Entrenador'}),
            'horarios': forms.TextInput(attrs={'class': 'input_uni'}),
        }

class SignupUser(forms.ModelForm):
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
            'genero': 'Género:',
            'correo': 'E-mail:',
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de teléfono'}),
            'edad': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Edad'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
            'genero': forms.TextInput(attrs={'class':'input_radio'}),
            'correo': forms.EmailInput(attrs={'class':'input_uni', 'placeholder': 'E-mail'}),
        }



        


















