from django import forms


class SignupAdmin(forms.Form):
    identificacion_propietario = forms.IntegerField(
        label="Identificación del Propietario:",
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Identificación del Propietario'}),
        required=True
    )
    documento = forms.IntegerField(
        label="Documento:",
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
        required=True
    )
    nombre_admin = forms.CharField(
        label="Nombre:",
        max_length=40,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre de Administrador'}),
        required=True
    )
    apellido_admin = forms.CharField(
        label="Apellido:",
        max_length=40,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
        required=True
    )
    telefono = forms.CharField(
        label="Teléfono:",
        max_length=14,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'+(57) --- --- ----'}),
        required=True
    )
    direccion = forms.CharField(
        label="Dirección:",
        max_length=75,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Dirección'}),
        required=True
    )
    correo = forms.EmailField(
        label="Correo Electrónico:",
        max_length=75,
        widget=forms.EmailInput(attrs={'class':'input_uni', 'placeholder':'Correo Electrónico'}),
        required=True
    )
    contrasena_admin = forms.CharField(
        label="Contraseña de Administrador:",
        min_length=10,  # Manteniendo la longitud mínima
        max_length=40,  # Manteniendo la longitud máxima
        widget=forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña de Administrador'}),
        required=True
    )

class SignupCoach(forms.Form):
    documento = forms.IntegerField(
        label="Documento:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Numero de Documento'}),
        required=True
    )
    nombre = forms.CharField(
        label="Nombre:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
        required=True
    )
    apellido = forms.CharField(
        label="Apellido:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
        required=True
    )
    direccion = forms.CharField(
        label="Dirección:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Dirección'}),
        required=True
    )
    edad = forms.CharField(
        label="Edad:",
 
        widget=forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Edad'}),
        required=True
    )


    telefono = forms.CharField(
        label="Teléfono:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'+(57) --- --- ----'}),
        required=True
    )

    correo = forms.EmailField(
        label="Correo Electrónico:",

        widget=forms.EmailInput(attrs={'class':'input_uni', 'placeholder':'E-mail'}),
        required=True
    )
    genero_choices = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]    
    genero = forms.ChoiceField(
        label="Género:",
        choices=genero_choices,
        widget=forms.RadioSelect(attrs={'class': 'input_radio'}),
        required=True
    )

    contrasena = forms.CharField(
        label="Contraseña:",

        widget=forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
        required=True
    )

    ficha_de_ingreso = forms.CharField(
        label="Ficha de Entrenador:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Ficha de Entrenador'}),
        required=True
    )
    experiencia = forms.CharField(
        label="Experiencia:",
 
        widget=forms.TextInput(attrs={'class': 'input_uni', 'placeholder': 'Experiencia'}),
        required=True
    )

    especializacion = forms.ChoiceField(
        label="Especialización:",
        choices=(
            ('', 'Seleccione su especialización'),  # Opción vacía por defecto
            ('Fitness', 'Fitness'),
            ('Pilates', 'Pilates'),
            ('Rehabilitacion fisica', 'Rehabilitacion fisica'),
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
            ('', 'Seleccione un horario'),  # Opción vacía por defecto
            ('Mañana (5:00am - 8:00am)', 'Mañana (5:00am - 8:00am)'),
            ('Tarde (2:00pm - 5:00pm)', 'Tarde (2:00pm - 5:00pm)'),
            ('Noche (6:00pm - 9:00pm)', 'Noche (6:00pm - 9:00pm)'),
            ('Madrugada (10:00pm - 1:00am)', 'Madrugada (10:00pm - 1:00am)')
        ),
        widget=forms.Select(attrs={'class':'input_uni'}),
        required=True
    )


class SignupUser(forms.Form):
    documento = forms.IntegerField(
        label="Documento:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Numero de Documento'}),
        required=True
        )
    nombre = forms.CharField(
        label="Nombre:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre'}),
        required=True
    )
    apellido = forms.CharField(
        label="Apellido:",
 
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
        required=True
    )
    telefono = forms.CharField(
        label="Número de teléfono:",

        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de teléfono'}),
        required=True
    )
    edad = forms.CharField(
        label="Edad:",
  
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Edad'}),
        required=True
    )
    contrasena = forms.CharField(
        label="Contraseña:",

        widget=forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña'}),
        required=True
    )
    # contraseña2 = forms.CharField(
    #     label="Repita contraseña:",
    #     min_length=10,
    #     max_length=40,
    #     widget=forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Repita contraseña'}),
    #     required=True
    # )
    genero = forms.ChoiceField(
        label="Género:",
        choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],
        widget=forms.RadioSelect(attrs={'class':'input_radio'}),
        required=True
    )


 

