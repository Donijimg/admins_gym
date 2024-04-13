from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .form_signup import SignupAdmin,SignupCoach,SignupUser
from .models import Admin,Coach,UserRegistration,ClientRoutine
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def signup_opcion(request):
    return render(request, 'opcions/signup_opcion.html', {})

def login_opcion(request):
    return render(request, 'opcions/login_opcion.html', {})

def signup_ad(request):
    if request.method == 'POST':
        admin_form = SignupAdmin(request.POST)
        if admin_form.is_valid():
            # Procesar los datos del formulario
            identificacion_propietario = admin_form.cleaned_data['identificacion_propietario']
            documento = admin_form.cleaned_data['documento']
            nombre_admin = admin_form.cleaned_data['nombre_admin']
            apellido_admin = admin_form.cleaned_data['apellido_admin']
            telefono = admin_form.cleaned_data['telefono']
            correo = admin_form.cleaned_data['correo']
            direccion = admin_form.cleaned_data['direccion']
            contrasena_admin = admin_form.cleaned_data['contrasena_admin']
            
            # Guardar el administrador en la base de datos
            admin = Admin.objects.create(
                identificacion_propietario=identificacion_propietario,
                documento=documento,
                nombre_admin=nombre_admin,
                apellido_admin=apellido_admin,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                contrasena_admin=contrasena_admin
            )

            # Iniciar sesión automáticamente después del registro
            login(request, admin)
            
            return redirect('logeado_ad')  # Redirigir a la página de inicio después del registro
    else:
        admin_form = SignupAdmin()

    return render(request, 'signups/signup_administrador.html', {'admin_form': admin_form})

@login_required
def logeado_ad(request):
    coachs = Coach.objects.all()
    clientes = UserRegistration.objects.all()
    
    # Renderizar la plantilla 'logeado_ad/logeado_ad.html' con los entrenadores y clientes en el contexto
    return render(request, 'logeado_ad/logeado_ad.html', {'coachs': coachs, 'clientes': clientes})



def index(request):
    return render(request, 'layouts/app.html', {})


def profile_ad(request):
    return render(request, 'profile/profile_ad.html', {})

def profile_en(request):
    return render(request, 'profile/profile_en.html', {})

def profile_cl(request):
    return render(request, 'profile/profile_cl.html', {})


def galeria_ver(request):
    return render(request, 'galeria_ver.html', {})

#more imformation





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





def inscribirse(request, especializacion, id):
    # Verificar si el usuario está autenticado
    if not request.user.is_authenticated:
        # Si el usuario no está autenticado, redirigirlo a la página de inicio de sesión
        return redirect('login_cl')  # Reemplaza 'login' con el nombre de tu vista de inicio de sesión

    # Obtener el entrenador
    coach = get_object_or_404(Coach, pk=id, especializacion=especializacion)
    # Obtener el usuario autenticado
    usuario = request.user
    # Verificar si el usuario ya está inscrito en la rutina del entrenador
    inscrito = ClientRoutine.objects.filter(entrenador=coach, usuario=usuario).exists()
    if not inscrito:
        # Si el usuario no está inscrito, crear una nueva instancia de ClientRoutine
        cliente = ClientRoutine(entrenador=coach, usuario=usuario)
        cliente.save()
        # Redirigir o renderizar la respuesta adecuada
        return redirect('página_de_destino_después_de_inscribirse')
    else:
        # Si el usuario ya está inscrito, mostrar un mensaje de error o redirigir a alguna página
        messages.error(request, "Ya estás inscrito en esta rutina.")
        return redirect('página_de_destino_después_de_error')


# Vista para mostrar la lista de entrenadores y sus especializaciones
def list_clientes_entrenador(request):
    # Obtener todos los entrenadores con especialización 'Fitness'
    coachs_fitness = Coach.objects.filter(especializacion='Fitness')
    return render(request, 'list/list_clientes_entrenador.html', {'coachs_fitness': coachs_fitness})

# Vista para mostrar los detalles del entrenador y la lista de clientes inscritos
def detalle_cliente_fitness(request, coach_id):
    # Obtener el entrenador
    coach = get_object_or_404(Coach, pk=coach_id)
    # Obtener la lista de clientes inscritos en la clase del entrenador
    clientes = ClientRoutine.objects.filter(entrenador=coach)
    return render(request, 'list/detalle_cliente_fitness.html', {'coach': coach, 'clientes': clientes})




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
    return render(request,'dietas/dietas.html',{})

def vista_dietas(request):
    return render(request, 'dietas/vista_dietas.html',{})

def dietas_cl(request):
    return render(request,'dietas/dietas_cl.html',{})

def vista_dietas_cl(request):
    return render(request, 'dietas/vista_dietas_cl.html',{})


def dietas_en(request):
    return render(request,'dietas/dietas_en.html',{})

def dietas_ad(request):
    return render(request,'dietas/dietas_ad.html',{})

def vista_dietas_ad(request):
    return render(request, 'dietas/vista_dietas_ad.html',{})

def vista_dietas_en(request):
    return render(request, 'dietas/vista_dietas_en.html',{})


def ampliada_crear(request):
    return render(request, 'dietas/vista_ampliada.html',{})
def ampliada_editar(request):
    return render(request, 'dietas/vista_ampliada.html',{})
def ampliada_eliminar(request):
    return render(request, 'dietas/vista_ampliada.html',{})






def galeria_one(request):
    return render(request,'galeria/galeria1.html',{})
def galeria_two(request):
    return render(request,'galeria/galeria2.html',{})
def galeria_three(request):
    return render(request,'galeria/galeria3.html',{})
def galeria_four(request):
    return render(request,'galeria/galeria4.html',{})
def galeria_five(request):
    return render(request,'galeria/galeria5.html',{})



def acercade(requets):
    return render(requets,'imfo/acercade.html',{})
def acercade_ad(requets):
    return render(requets,'imfo/acercade_ad.html',{})
def acercade_cl(requets):
    return render(requets,'imfo/acercade_cl.html',{})
def acercade_en(requets):
    return render(requets,'imfo/acercade_en.html',{})





# entrenadores_con_mismo_nombre = Coach.objects.filter(nombre_usuario=nombre_usuario)
#     if entrenadores_con_mismo_nombre.exists():
#         # Informar al usuario que el nombre de usuario ya está en uso
#         return render(request, 'signup_entrenador.html', {'error_message': 'El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario.'})




# def logeado_ad(request):
#     coachs = Coach.objects.all()
#     clientes = UserRegistration.objects.all()
    
#     # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
#     return render(request, 'logeado_ad/logeado_ad.html', {'coachs': coachs, 'clientes': clientes})


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





# toca hacer vañidaciones y credenciales
def signup_cl(request):
    if request.method == 'POST':
        user = SignupUser(request.POST)
        if user.is_valid():
            # Procesar y guardar los datos del formulario
            documento = user.cleaned_data['documento']
            nombre = user.cleaned_data['nombre']
            apellido = user.cleaned_data['apellido']
            telefono = user.cleaned_data['telefono']
            edad = user.cleaned_data['edad']
            contrasena = user.cleaned_data['contrasena']
            genero = user.cleaned_data['genero']
            
            # Guardar el usuario en la base de datos
            user_save = UserRegistration.objects.create(
                documento=documento,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                edad=edad,
                contrasena=contrasena,
                genero=genero
            )
            
            return render(request, 'welcome/welcome_cl.html', {'user_save': user_save})
    else:
        user = SignupUser()
    
    return render(request, 'signups/signup_cliente.html', {'user': user})






# def signup_ad(request):
#     if request.method == 'POST':
#         admin = SignupAdmin(request.POST)
#         if admin.is_valid():
#             # Procesa los datos del formulario y guarda el administrador
#             identificacion_propietario = admin.cleaned_data['identificacion_propietario']
#             documento = admin.cleaned_data['documento']
#             nombre_admin = admin.cleaned_data['nombre_admin']
#             apellido_admin = admin.cleaned_data['apellido_admin']
#             telefono = admin.cleaned_data['telefono']
#             correo = admin.cleaned_data['correo']
#             direccion = admin.cleaned_data['direccion']
#             contrasena_admin = admin.cleaned_data['contrasena_admin']
            
#             # Guarda el administrador en la base de datos
#             admin_save = Admin.objects.create(
#                 identificacion_propietario=identificacion_propietario,
#                 documento=documento,
#                 nombre_admin=nombre_admin,
#                 apellido_admin=apellido_admin,
#                 telefono=telefono,
#                 correo=correo,
#                 direccion=direccion,
#                 contrasena_admin=contrasena_admin
#             )
            
#             return render(request, 'welcome/welcome_ad.html', {'admin_save': admin_save})
#     else:
#         admin = SignupAdmin()

    
#     return render(request, 'signups/signup_administrador.html', {'admin': admin})

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




def login_ad(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        contrasena_admin = request.POST.get('contrasena_admin')

        # Buscar al administrador por identificacion_propietario
        admin = Admin.objects.filter(identificacion_propietario=identificacion_propietario).first()

        if admin is not None and admin.contrasena_admin == contrasena_admin:
            # Las credenciales son válidas, inicia sesión
            # Aquí puedes agregar la lógica de iniciar sesión manualmente si es necesario
            return render(request, 'welcome/welcome_ad.html')
        else:
            # Las credenciales son inválidas, muestra un mensaje de error o renderiza nuevamente el formulario de inicio de sesión
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
        nombre = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del cliente
        try:
            user = UserRegistration.objects.get(nombre=nombre, contrasena=contrasena)
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



#ver la rutina
#guardar la rutina
#eliminar datos de la misma
#editar datos de la misma

