from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
from .forms import SignupAdmin,SignupCoach,SignupUser,InscripcionUser
from .models import Admin,Coach,User,Inscripcion
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
# from django.http import HttpResponseRedirect

def signup_opcion(request):
    return render(request, 'opcions/signup_opcion.html', {})

def login_opcion(request):
    return render(request, 'opcions/login_opcion.html', {})

def signup_ad(request):
    if request.method == 'POST':
        admin_form = SignupAdmin(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('welcome_ad')
    else:
        admin_form = SignupAdmin() 
    return render(request, 'signups/signup_administrador.html', {'admin_form': admin_form})

def signup_en(request):
    if request.method == 'POST':
        coach_form = SignupCoach(request.POST)
        if coach_form.is_valid():
            coach_form.save()  # Guarda el objeto Coach en la base de datos
            return redirect('welcome_en')  # Redirigir al usuario a la página de bienvenida para entrenadores
    else:
        coach_form = SignupCoach()
    return render(request, 'signups/signup_entrenador.html', {'coach_form': coach_form})


def signup_cl(request):
    if request.method == 'POST':
        user_form = SignupUser(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('welcome_cl')  # Redirigir al usuario a la página de bienvenida para clientes
    else:
        user_form = SignupUser()
    return render(request, 'signups/signup_cliente.html', {'user_form': user_form})

def welcome_ad(request):
    return render(request, 'welcome/welcome_ad.html')
def welcome_en(request):
    return render(request, 'welcome/welcome_en.html')
def welcome_cl(request):
    return render(request, 'welcome/welcome_cl.html')




def logeado_ad(request):
    coachs = Coach.objects.all()
    clientes = User.objects.all()
    
    # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
    return render(request, 'logeado_ad/logeado_ad.html', {'coachs': coachs, 'clientes': clientes})




def logeado_en(request):
    # Obtener todos los entrenadores de la base de datos
    coachs = Coach.objects.all()
    clientes = User.objects.all()
    # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
    return render(request, 'logeado_en/logeado_en.html', {'clientes': clientes,'coachs': coachs,})



def logeado_cl(request):
  coachs = Coach.objects.all()
  # Renderizar la plantilla 'logeado/logeado_en.html' con los entrenadores en el contexto
  return render(request, 'logeado_cl/logeado_cl.html', {'coachs': coachs})
    
    

def login_ad(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        contrasena_admin = request.POST.get('contrasena_admin')


        user = authenticate(identificacion_propietario=identificacion_propietario, contrasena_admin=contrasena_admin)
        
        if user is not None:

            # login(request, user)
            return redirect('logeado_ad') 
        else:

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
            user = User.objects.get(nombre=nombre, contrasena=contrasena)
            # Si las credenciales son válidas, se puede redirigir o mostrar un mensaje de éxito
            return render(request, 'welcome/welcome_cl.html')
        except User.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'logins/login_cliente.html', {'error': True})

    return render(request, 'logins/login_cliente.html', {})


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

#vista del adminisitrador lista entrenadores y clientes 
 
def list_all_fitness(request):
    coachs_fitness = Coach.objects.filter(especializacion='Fitness')
    inscripciones_fitness = Inscripcion.objects.filter(inscripcion='Fitness')
    usuarios_fitness = [inscripcion.usuario for inscripcion in inscripciones_fitness]
    return render(request, 'list/views_admin/list_all_fitness.html', {'coachs_fitness': coachs_fitness, 'usuarios_fitness': usuarios_fitness})

def list_all_pilates(request):
    coachs_pilates = Coach.objects.filter(especializacion='Pilates')
    inscripciones_pilates = Inscripcion.objects.filter(inscripcion='Pilates')
    usuarios_pilates = [inscripcion.usuario for inscripcion in inscripciones_pilates]
    return render(request, 'list/views_admin/list_all_pilates.html', {'coachs_pilates': coachs_pilates, 'usuarios_pilates': usuarios_pilates})

def list_all_rehabilitacion(request):
    coachs_rehabilitacion = Coach.objects.filter(especializacion='Rehabilitacion fisica')
    inscripciones_rehabilitacion = Inscripcion.objects.filter(inscripcion='Rehabilitacion fisica')
    usuarios_rehabilitacion = [inscripcion.usuario for inscripcion in inscripciones_rehabilitacion]
    return render(request, 'list/views_admin/list_all_rehabilitacion.html', {'coachs_rehabilitacion': coachs_rehabilitacion, 'usuarios_rehabilitacion': usuarios_rehabilitacion})

def list_all_mayores(request):
    coachs_mayores = Coach.objects.filter(especializacion='Plan para mayores')
    inscripciones_mayores = Inscripcion.objects.filter(inscripcion='Plan para mayores')
    usuarios_mayores = [inscripcion.usuario for inscripcion in inscripciones_mayores]
    return render(request, 'list/views_admin/list_all_mayores.html', {'coachs_mayores': coachs_mayores, 'usuarios_mayores': usuarios_mayores})

def list_all_yoga(request):
    coachs_yoga = Coach.objects.filter(especializacion='Yoga')
    inscripciones_yoga = Inscripcion.objects.filter(inscripcion='Yoga')
    usuarios_yoga = [inscripcion.usuario for inscripcion in inscripciones_yoga]
    return render(request, 'list/views_admin/list_all_yoga.html', {'coachs_yoga': coachs_yoga, 'usuarios_yoga': usuarios_yoga})

def list_all_gimnacia(request):
    coachs_fitness = Coach.objects.filter(especializacion='Gimnacia')
    inscripciones_fitness = Inscripcion.objects.filter(inscripcion='Gimnacia')
    usuarios_fitness = [inscripcion.usuario for inscripcion in inscripciones_fitness]
    return render(request, 'list/views_admin/list_all_gimnacia.html', {'coachs_fitness': coachs_fitness, 'usuarios_fitness': usuarios_fitness})




#vistas para listar clientes para entrenadores

def list_clientes_fitness(request):
    inscripciones_fitness = Inscripcion.objects.filter(inscripcion='Fitness')
    usuarios_fitness = [inscripcion.usuario for inscripcion in inscripciones_fitness]
    return render(request, 'list/views_coachs/list_clientes_fitness.html', {'usuarios_fitness': usuarios_fitness}) 

def detalle_cliente_fitness(request, inscripcion):
    usuario = get_object_or_404(User, id=inscripcion)  # Suponiendo que 'Usuario' es el modelo para tus clientes de fitness
    return render(request, 'list/views_coachs/detalle_cliente_fitness.html', {'usuario': usuario})

def list_clientes_pilates(request):
    inscripciones_pilates = Inscripcion.objects.filter(inscripcion='Pilates')
    usuarios_piltes = [inscripcion.usuario for inscripcion in inscripciones_pilates]
    return render(request, 'list/views_coachs/list_clientes_gimnacia.html', {'usuarios_piltes': usuarios_piltes})

def list_clientes_rehabilitacion(request):
    inscripciones_rehabilitacion = Inscripcion.objects.filter(inscripcion='Rehabilitacion fisica')
    usuarios_rehabilitacion = [inscripcion.usuario for inscripcion in inscripciones_rehabilitacion]
    return render(request, 'list/views_coachs/list_clientes_rehabilitacion.html', {'usuarios_rehabilitacion': usuarios_rehabilitacion})


def list_clientes_mayores(request):
    inscripciones_mayores = Inscripcion.objects.filter(inscripcion='Plan para mayores')
    usuarios_mayores = [inscripcion.usuario for inscripcion in inscripciones_mayores]
    return render(request, 'list/views_coachs/list_clientes_mayores.html', {'usuarios_mayores': usuarios_mayores})

def list_clientes_yoga(request):
    inscripciones_yoga = Inscripcion.objects.filter(inscripcion='Yoga')
    usuarios_yoga = [inscripcion.usuario for inscripcion in inscripciones_yoga]
    return render(request, 'list/views_coachs/list_clientes_yoga.html', {'usuarios_yoga': usuarios_yoga})

def list_clientes_gimnacia(request):
    inscripciones_gimnacia = Inscripcion.objects.filter(inscripcion='Gimnacia')
    usuarios_gimnacia = [inscripcion.usuario for inscripcion in inscripciones_gimnacia]
    return render(request, 'list/views_coachs/list_clientes_gimnacia.html', {'usuarios_gimnacia': usuarios_gimnacia})





def detalle_inscripcion_gimnacia(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_gimnacia.html', {'inscripcion': inscripcion})


def detalle_inscripcion_mayores(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_mayores.html', {'inscripcion': inscripcion})


def detalle_inscripcion_fitness(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_fitness.html', {'inscripcion': inscripcion})


def detalle_inscripcion_pilates(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_pilates.html', {'inscripcion': inscripcion})


def detalle_inscripcion_rehabilitacion(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_rehabilitacion.html', {'inscripcion': inscripcion})



def detalle_inscripcion_yoga(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    inscripcion = Inscripcion.objects.get(usuario=usuario)
    return render(request, 'detalle_inscripcion_yoga.html', {'inscripcion': inscripcion})

#vistas para listar entrenadores para clientes
# En views.py


def detalle_coachs_fitness(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)

    if request.method == 'POST':
        inscripcion_form = InscripcionUser(request.POST)
        if inscripcion_form.is_valid():
            # Guarda la inscripción del usuario
            inscripcion_form.save()
            # Redirige a donde quieras después de la inscripción
            return redirect('página_de_inicio')  
    else:
        inscripcion_form = InscripcionUser()

    return render(request, 'list/views_cliente/detalle_coachs_fitness.html', {'coach': coach, 'inscripcion_form': inscripcion_form})




def list_coachs_fitness(request, typo_id):
    coachs_fitness = Coach.objects.filter(especializacion=typo_id)
    return render(request, 'list/views_cliente/list_coachs_fitness.html', {'coachs_fitness': coachs_fitness})


def detalle_coachs_fitness(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_fitness.html', {'coach': coach})


def list_coachs_pilates(request):
    coachs_fitness = Coach.objects.filter(especializacion='Pilates')
    return render(request, 'list/views_cliente/list_coachs_pilates.html', {'coachs_fitness': coachs_fitness})

def detalle_coachs_pilates(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_pilates.html', {'coach': coach})

def list_coachs_rehabilitacion(request):
    coachs_rehabilitacion = Coach.objects.filter(especializacion='Rehabilitacion fisica')
    return render(request, 'list/views_cliente/list_coachs_rehabilitacion.html', {'coachs': coachs_rehabilitacion})

def detalle_coachs_rehabilitacion(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_rehabilitacion.html', {'coach': coach})

def list_coachs_mayores(request):
    coachs_mayores = Coach.objects.filter(especializacion='Plan para mayores')
    return render(request, 'list/views_cliente/list_coachs_mayores.html', {'coachs_mayores': coachs_mayores})

def detalle_coachs_mayores(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_mayores.html', {'coach': coach})

def list_coachs_yoga(request):
    coachs_yoga = Coach.objects.filter(especializacion='Yoga')
    return render(request, 'list/views_cliente/list_coachs_yoga.html', {'coachs_yoga': coachs_yoga})

def detalle_coachs_yoga(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_yoga.html', {'coach': coach})

def list_coachs_gimnasia(request):
    coachs_gimnasia = Coach.objects.filter(especializacion='Gimnasia')
    return render(request, 'list/views_cliente/list_coachs_gimnasia.html', {'coachs_gimnasia': coachs_gimnasia})

def detalle_coachs_gimnasia(request, especialization, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id, especializacion=especialization)
    return render(request, 'list/views_cliente/detalle_coachs_gimnasia.html', {'coach': coach})















# En tus vistas




def eliminar_entrenador_por_documento(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        entrenador = Coach.objects.filter(documento=documento).first()
        if entrenador:
            entrenador.delete()
            messages.success(request, 'Entrenador eliminado exitosamente.')
            return redirect('mostrar_mensaje', tipo='exito')  # Redirigir a la página de éxito
        else:
            messages.error(request, 'No se encontró ningún entrenador con el documento proporcionado.')
            return redirect('mostrar_mensaje', tipo='error')  # Redirigir a la página de error
    else:
        return redirect('mostrar_mensaje', tipo='error')

def eliminar_cuenta_por_documento(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        usuario = User.objects.filter(documento=documento).first()
        if usuario:
            usuario.delete()
            messages.success(request, 'Cuenta de usuario eliminada exitosamente.')
            return redirect('mostrar_mensaje', tipo='exito')  # Redirigir a la página de éxito
        else:
            messages.error(request, 'No se encontró ninguna cuenta de usuario con el documento proporcionado.')
            return redirect('mostrar_mensaje', tipo='error')  # Redirigir a la página de error
    else:
        return redirect('mostrar_mensaje', tipo='error')

def mostrar_mensaje(request, tipo):
    mensaje = 'Entrenador eliminado exitosamente.' if tipo == 'exito' else 'No se encontró ningún entrenador con el documento proporcionado.'
    return render(request, 'list/views_admin/mostrar_mensaje.html', {'mensaje': mensaje, 'tipo': tipo})






# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                         START ADMIN PROFILE                                                                              #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#


def eliminar_admin(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        admin = Admin.objects.filter(identificacion_propietario=identificacion_propietario).first()
        if admin:
            admin.delete()
            messages.success(request, 'Administrador eliminado correctamente.')
        else:
            messages.error(request, 'No se encontró ningún administrador con la identificación proporcionada.')
        return redirect('index')

    return redirect('index')#<===============================================================================  # MENTERIO EJEMPLO


def buscar_admin(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        admin = Admin.objects.filter(identificacion_propietario=identificacion_propietario).first()
        if admin:
            return render(request, 'profile/profile_ad.html', {'admin': admin})
        else:
            messages.error(request, 'No se encontró ningún administrador con la identificación proporcionada.')
            return redirect('info_admin')
    else:
        return render(request, 'profile/profile_ad.html')


def ingresar_admin(request):
    return render(request, 'profile/profile_ad.html')


def actualizar_admin(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        admin = Admin.objects.filter(identificacion_propietario=identificacion_propietario).first()
        if admin:
            
            admin.nombre_admin = request.POST.get('nombre_admin')
            admin.apellido_admin = request.POST.get('apellido_admin')
           
            admin.save()
            messages.success(request, 'Información del administrador actualizada correctamente.')
            return redirect('index') 
        else:
            messages.error(request, 'No se encontró ningún administrador con la identificación proporcionada.')
            return redirect('actualizar_admin') 
    else:
        return render(request, 'profile/profile_ad.html')

# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                        FINISH ADMIN PROFILE                                                                              #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#
# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                         START COACH PROFILE                                                                              #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#


def eliminar_coach(request):
    if request.method == 'POST':
        ficha_de_ingreso = request.POST.get('ficha_de_ingreso')
        coach = Coach.objects.filter(ficha_de_ingreso=ficha_de_ingreso).first()
        if coach:
            coach.delete()
            messages.success(request, 'Coach eliminado correctamente.')
        else:
            messages.error(request, 'No se encontró ningún coach con la ficha de ingreso proporcionado.')
        return redirect('index')
    return redirect('index')


def buscar_coach(request):
    if request.method == 'POST':
        ficha_de_ingreso = request.POST.get('ficha_de_ingreso')
        coach = Coach.objects.filter(ficha_de_ingreso=ficha_de_ingreso).first()
        print(coach)
        if coach:
            return render(request, 'profile/profile_en.html', {'coach': coach})
        else:
            messages.error(request, 'No se encontró ningún coach con la ficha de ingreso proporcionado.')
            return render(request, 'profile/profile_en.html')
    else:
        return render(request, 'profile/profile_en.html')


def ingresar_coach(request):
    return render(request, 'profile/profile_en.html')


def actualizar_coach(request):
    if request.method == 'POST':
        ficha_de_ingreso = request.POST.get('ficha_de_ingreso')
        coach = Coach.objects.filter(ficha_de_ingreso=ficha_de_ingreso).first()
        if coach:
            coach.nombre = request.POST.get('nombre')
            coach.apellido = request.POST.get('apellido')
            # Actualiza otros campos de manera similar

            coach.save()
            messages.success(request, 'Información del coach actualizada correctamente.')
            return redirect('index')
        else:
            messages.error(request, 'No se encontró ningún coach con la ficha de ingreso proporcionado.')
            return redirect('actualizar_coach')
    else:
        return render(request, 'profile/profile_en.html')



# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                        FINISH COACH PROFILE                                                                              #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#






# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                         START USER PROFILE                                                                               #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#


def eliminar_user(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        user = User.objects.filter(documento=documento).first()
        if user:
            user.delete()
            messages.success(request, 'Usuario eliminado correctamente.')
        else:
            messages.error(request, 'No se encontró ningún usuario con el documento proporcionado.')
        return redirect('index')
    return redirect('index')


def buscar_user(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        user = User.objects.filter(documento=documento).first()
        print(user)
        if user:
            return render(request, 'profile/profile_cl.html', {'user': user})
        else:
            messages.error(request, 'No se encontró ningún usuario con el documento proporcionado.')
            return render(request, 'profile/profile_cl.html')
    else:
        return render(request, 'profile/profile_cl.html')




def ingresar_user(request):
    return render(request, 'profile/profile_cl.html')


def actualizar_user(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        user = User.objects.filter(documento=documento).first()
        if user:
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            # Actualiza otros campos de manera similar

            user.save()
            messages.success(request, 'Información del usuario actualizada correctamente.')
            return redirect('index')
        else:
            messages.error(request, 'No se encontró ningún usuario con el documento proporcionado.')
            return redirect('actualizar_user')
    else:
        return render(request, 'profile/profile_cl.html')



















# =========================================================================================================================================================================#
#                                                                                                                                                                          #
#                                                                        FINISH USER PROFILE                                                                               #
#                                                                                                                                                                          #
# =========================================================================================================================================================================#


def vista_dietas_fitness(request):
    return render(request, 'dietas/vista_dietas_fitness.html',{})

def vista_dietas_pilates(request):
    return render(request, 'dietas/vista_dietas_pilates.html',{})

def vista_dietas_rehabilitacion(request):
    return render(request, 'dietas/vista_dietas_rehabilitacion.html',{})

def vista_dietas_mayores(request):
    return render(request, 'dietas/vista_dietas_mayores.html',{})

def vista_dietas_yoga(request):
    return render(request, 'dietas/vista_dietas_yoga.html',{})
def vista_dietas_gimnasia(request):
    return render(request, 'dietas/vista_dietas_gimnasia.html',{})




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

