from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .form_signup import SignupAdmin,SignupCoach,SignupUser

from .models import Admin,Coach,UserRegistration,ClientRoutine



def signup_cl(request):
    if request.method == 'POST':
        user = SignupUser(request.POST)
        if user.is_valid():
            # Verificar si las contraseñas coinciden
            contraseña = user.cleaned_data['contraseña']
            contraseña2 = user.cleaned_data['contraseña2']
            if contraseña != contraseña2:
                user.add_error('contraseña2', 'Las contraseñas no coinciden')
            else:
                # Procesar y guardar los datos del formulario
                documento = user.cleaned_data['documento']
                nombre = user.cleaned_data['nombre']
                apellido = user.cleaned_data['apellido']
                telefono = user.cleaned_data['telefono']
                edad = user.cleaned_data['edad']
                contraseña = user.cleaned_data['contraseña']
                genero = user.cleaned_data['genero']
                
                # Guardar el usuario en la base de datos
                user_save = UserRegistration.objects.create(
                    documento=documento,
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    edad=edad,
                    contraseña=contraseña,
                    genero=genero
                )
                
                return render(request, 'welcome/welcome_cl.html', {'user_save': user_save})
    else:
        user = SignupUser()
    
    return render(request, 'signups/signup_cliente.html', {'user': user})




def signup_ad(request):
    if request.method == 'POST':
        admin = SignupAdmin(request.POST)
        if admin.is_valid():
            # Procesa los datos del formulario y guarda el administrador
            identificacion_propietario = admin.cleaned_data['identificacion_propietario']
            documento = admin.cleaned_data['documento']
            nombre_admin = admin.cleaned_data['nombre_admin']
            apellido_admin = admin.cleaned_data['apellido_admin']
            telefono = admin.cleaned_data['telefono']
            correo = admin.cleaned_data['correo']
            direccion = admin.cleaned_data['direccion']
            contrasena_admin = admin.cleaned_data['contrasena_admin']
            
            # Guarda el administrador en la base de datos
            admin_save = Admin.objects.create(
                identificacion_propietario=identificacion_propietario,
                documento=documento,
                nombre_admin=nombre_admin,
                apellido_admin=apellido_admin,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                contrasena_admin=contrasena_admin
            )
            
            return render(request, 'welcome/welcome_ad.html', {'admin_save': admin_save})
    else:
        admin = SignupAdmin()

    
    return render(request, 'signups/signup_administrador.html', {'admin': admin})


def signup_en(request):
    if request.method == 'POST':
        coach = SignupCoach(request.POST)
        
        if coach.is_valid():
            # Procesar y guardar los datos del formulario
            documento = coach.cleaned_data['documento']
            nombre = coach.cleaned_data['nombre']
            apellido = coach.cleaned_data['apellido']
            direccion = coach.cleaned_data['direccion']
            edad = coach.cleaned_data['edad']
            telefono = coach.cleaned_data['telefono']
            correo = coach.cleaned_data['correo']
            genero = coach.cleaned_data['genero']
            contrasena = coach.cleaned_data['contrasena']
            ficha_de_ingreso = coach.cleaned_data['ficha_de_ingreso']
            experiencia = coach.cleaned_data['experiencia']
            especializacion = coach.cleaned_data['especializacion']
            horarios = coach.cleaned_data['horarios']
            
            # Guardar el entrenador en la base de datos
            coach_save = Coach.objects.create(
                documento=documento,
                nombre=nombre,
                apellido=apellido,
                direccion=direccion,
                edad=edad,
                telefono=telefono,
                correo=correo,
                genero=genero,
                contrasena=contrasena,
                ficha_de_ingreso=ficha_de_ingreso,
                experiencia=experiencia,
                especializacion=especializacion,
                horarios=horarios
            )
            
            return render(request, 'welcome/welcome_en.html', {'coach_save': coach_save})
    else:
        coach = SignupCoach()
    
    return render(request, 'signups/signup_entrenador.html', {
        'coach': coach,
    })

def index(request):
    return render(request, 'layouts/app.html', {})

def logeado_ad(request):
    coachs = Coach.objects.all()
    clientes = UserRegistration.objects.all()
    
    # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
    return render(request, 'logeado_ad/logeado_ad.html', {'coachs': coachs, 'clientes': clientes})


def logeado_en(request):
    # Obtener todos los entrenadores de la base de datos
    coachs = Coach.objects.all()
    clientes = UserRegistration.objects.all()
    # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
    return render(request, 'logeado_en/logeado_en.html', {'clientes': clientes,'coachs': coachs,})



def logeado_cl(request):
  coachs = Coach.objects.all()
  # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
  return render(request, 'logeado_cl/logeado_cl.html', {'coachs': coachs})
    
    


def signup_opcion(request):
    return render(request, 'opcions/signup_opcion.html', {})

def login_opcion(request):
    return render(request, 'opcions/login_opcion.html', {})



#vista user listas de entrenadores por area

def list_coachs_fitness(request):
    coachs = Coach.objects.filter(especializacion='Fitness')
    return render(request, 'list/list_coachs_fitness.html', {'coachs': coachs})

def detalle_coachs_fitness(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_fitness.html', {'coach': coach})

def list_coachs_pilates(request):
    coachs = Coach.objects.filter(especializacion='Pilates')
    return render(request, 'list/list_coachs_pilates.html', {'coachs': coachs})

def detalle_coachs_pilates(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_pilates.html', {'coach': coach})

def list_coachs_rehabilitacion(request):
    coachs = Coach.objects.filter(especializacion='Rehabilitacion fisica')
    return render(request, 'list/list_coachs_rehabilitacion.html', {'coachs': coachs})


def detalle_coachs_rehabilitacion(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_rehabilitacion.html', {'coach': coach})

# En el archivo views.py
# En tu archivo views.py



def inscribirse(request, especializacion, id):
    coach = get_object_or_404(Coach, pk=id, especializacion=especializacion)
    cliente = ClientRoutine(entrenador=coach, horarios=coach.horarios)
    cliente.save()
    return render(request, 'list/horarios.html', {'coach': coach})













def list_coachs_mayores(request):
    coachs = Coach.objects.filter(especializacion='Plan para mayores')
    return render(request, 'list/list_coachs_mayores.html', {'coachs': coachs})

def detalle_coachs_mayores(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_mayores.html', {'coach': coach})


def list_coachs_yoga(request):
    coachs = Coach.objects.filter(especializacion='Yoga')
    return render(request, 'list/list_coachs_yoga.html', {'coachs': coachs})


def detalle_coachs_yoga(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_yoga.html', {'coach': coach})


def list_coachs_gimnasia(request):
    coachs = Coach.objects.filter(especializacion='Gimnasia')
    return render(request, 'list/list_coachs_gimnasia.html', {'coachs': coachs})


def detalle_coachs_gimnasia(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/detalle_coachs_gimnasia.html', {'coach': coach})









#vista entrenador 
def detalle_user_fitness(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_fitness.html', {'user': user})

def detalle_user_pilates(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_pilates.html', {'user': user})

def detalle_user_rehabilitacion(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_rehabilitacion.html', {'user': user})

def detalle_user_mayores(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_mayores.html', {'user': user})

def detalle_user_yoga(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_yoga.html', {'user': user})

def detalle_user_gimnasia(request, user_id):
    user = get_object_or_404(UserRegistration, pk=user_id)
    return render(request, 'list/detalle_users_gimnasia.html', {'user': user})






def dietas(request):
    return render(request,'dietas.html',{})


def vista_ampliada(request):
    return render(request, 'vista_ampliada.html',{})



# entrenadores_con_mismo_nombre = Coach.objects.filter(nombre_usuario=nombre_usuario)
#     if entrenadores_con_mismo_nombre.exists():
#         # Informar al usuario que el nombre de usuario ya está en uso
#         return render(request, 'signup_entrenador.html', {'error_message': 'El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario.'})











def login_ad(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        contrasena_admin = request.POST.get('contrasena_admin')

        # Verificar las credenciales del administrador
        try:
            admin = Admin.objects.get(identificacion_propietario=identificacion_propietario, contrasena_admin=contrasena_admin)
            # Si las credenciales son válidas, se puede redirigir o mostrar un mensaje de éxito
            return render(request, 'welcome/welcome_ad.html')
        except Admin.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'logins/login_administrador.html', {'error': True})

    return render(request, 'logins/login_administrador.html', {})


def login_en(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del entrenador
        try:
            coach = Coach.objects.get(documento=documento, contrasena=contrasena)
            # Si las credenciales son válidas, renderizar la página de bienvenida
            return render(request, 'welcome/welcome_en.html')
        except Coach.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'logins/login_entrenador.html', {'error': True})

    return render(request, 'logins/login_entrenador.html', {})






def login_cl(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del cliente
        try:
            user = UserRegistration.objects.get(nombre_usuario=nombre_usuario, contrasena=contrasena)
            # Si las credenciales son válidas, se puede redirigir o mostrar un mensaje de éxito
            return render(request, 'welcome/welcome_cl.html')
        except UserRegistration.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'logins/login_cliente.html', {'error': True})

    return render(request, 'logins/login_cliente.html', {})




#views del entrenador

# def listar_modelo(request):
#     filtro_nombre= request.GET.get('nombre_campo')
#     repite lo mismo para los demas campos

#     objeto = modelo.objects.all()
# llama las tablas para poder acceder a sus datos 

#     if filtro_nombre:
#         objeto = objeto.filter(nombre_campo__icontains=filtro_nombre)

#     return render(request, 'listar_modelo.html', {'objeto': objeto, })

# def tabla_modelo(request):
#     return render(request, 'tabla_modelo.html', {})



# def editar_modelo(request, objeto_id):
#     objeto = modelo.objects.get(id=objeto_id)
#     if request.method == 'POST':
#         nombre_campo = request.POST['nombre_campo']
#         objeto.nombre_campo = nombre_campo
#         save_modelo(objeto)
#         return HttpResponse(f"Se actualizó el país {objeto.nombre_campo}.")
#     return render(request, 'editar_modelo.html', {'objeto': objeto})


# def recuperar_modelo(request):
#     objeto_id = request.GET['id']
#     objeto = modelo.objects.get(id=objeto_id)
#     save_modelo(objeto)
#     return render(request, 'recuperar_modelo.html', {'objeto': objeto})


# def eliminar_modelo(request):
#     objeto_id = request.GET['id']
#     objeto=modelo.objects.get(id=objeto_id).delete()
#     save_modelo(objeto)
#     return render(request, 'eliminar_modelo.html',{'objeto': objeto})


#views del del admin total
#ver la rutina
#guardar la rutina
#views del entrenador
#crear rutina
#eliminar datos de la misma
#recuperar datos de la misma
#editar datos de la misma
#ver rutina de empleador especifico






# views:

# listar_puestos.html:
# {% extends "layouts/app.html" %}
# {% block title %}
# <title>Listar Puestos</title>
# {% endblock title %}
# {% block card_title %}
# <h1>Listar Puestos</h1>
# {% endblock card_title %}
# {% block list %}
# {% include "forms/form_listar_puestos.html" %}
# {% endblock list %}

# form_listar_puestos.html :
# <section class="seccion_formulario">
#   <article class="card">
#     <form action="{% url 'listar_salarios' %}" method="get">
#       <div class="form-group">
#         <label for=""></label>
#         <input type="text" class="form-control" id="" name="" required>
#       </div>
#       <button type="submit">Buscar</button>
#     </form>
#   </article>
# </section>
# <table class="table">
#   <thead>
#     <tr>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for  in %}
#     <tr>
#       <td>{{}}</td>
#     </tr>
#     {% endfor %}
#   </tbody>
# </table>

# models: 
# necesito los archivos htlm corregidos y completados

# <!-- 
# <ul>
#   {% for empleado in empleados %}
#    <a href="#">Editar</a></li>
#   {% endfor %}
# </ul> -->
