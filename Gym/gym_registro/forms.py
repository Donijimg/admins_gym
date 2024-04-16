# forms.py
from django import forms
from .models import Admin, Coach, User

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
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
            'nombre': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
            'telefono': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de teléfono'}),
            'edad': forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Edad'}),
            'contrasena': forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
            'genero': forms.TextInput(attrs={'class':'input_radio'}),
        }



        


class LoginFormAdmin(forms.ModelForm):
    contrasena_admin = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ['identificacion_propietario', 'contrasena_admin']

    def clean(self):
        cleaned_data = super().clean()
        identificacion_propietario = cleaned_data.get('identificacion_propietario')
        contrasena_admin = cleaned_data.get('contrasena_admin')

        if identificacion_propietario and contrasena_admin:
            try:
                admin = Admin.objects.get(identificacion_propietario=identificacion_propietario)
            except Admin.DoesNotExist:
                raise forms.ValidationError('Las credenciales son inválidas. Por favor, inténtalo de nuevo.')

            if not admin.check_password(contrasena_admin):
                raise forms.ValidationError('Las credenciales son inválidas. Por favor, inténtalo de nuevo.')
        
        return cleaned_data