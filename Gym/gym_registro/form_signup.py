from django import forms


class SignupAdminPartOne(forms.Form):
    DNI_propietario = forms.IntegerField(
        label="Identificación del Propietario:",
        max_value=9999999,
        min_value=1000000,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Identificación del Propietario'}),
        required=True
    )
    Documento = forms.CharField(
        label="Documento:",
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Documento'}),
        required=True
    )
    Nombre_admin = forms.CharField(
        label="Nombre:",
        max_length=15,
        min_length=6,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Nombre de Administrador'}),
        required=True
    )
    Apellido_admin = forms.CharField(
        label="Apellido:",
        max_length=30,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Apellido'}),
        required=True
    )

class SignupAdminPartTwo(forms.Form):
    telefono = forms.CharField(
        label="Teléfono:",
        max_length=14,
        min_length=10,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Número de Teléfono'}),
        required=True
    )
    direccion = forms.CharField(
        label="Dirección:",
        max_length=75,
        min_length=10,
        widget=forms.TextInput(attrs={'class':'input_uni', 'placeholder':'Dirección'}),
        required=True
    )
    correo = forms.EmailField(
        label="Correo Electrónico:",
        max_length=75,
        min_length=20,
        widget=forms.EmailInput(attrs={'class':'input_uni', 'placeholder':'Correo Electrónico'}),
        required=True
    )
    contrasena_admin = forms.CharField(
        label="Contraseña de Administrador:",
        max_length=40,
        min_length=8,
        widget=forms.PasswordInput(attrs={'class':'input_uni', 'placeholder':'Contraseña de Administrador'}),
        required=True
    )











# class SignupCoach (forms.Form):
#     username =forms.CharField (
#     label="nombre",
#     max_length=30,
#     min_length=10,
#     widget=forms.TextInput(attrs={'class':'input'}), )

#     password = forms.IntegerField(
        
        
#     )

# class SignupUser (forms.Form):
#     username =forms.CharField (
#     label="nombre",
#     max_length=30,
#     min_length=10,
#     widget=forms.TextInput(attrs={'class':'input'}), )

#     password = forms.IntegerField('Password')