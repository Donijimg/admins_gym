from django.shortcuts import render,get_object_or_404,redirect
from .forms import SignupAdmin,SignupCoach,SignupUser,SolicitudesClienteForm
from .models import Admin,Coach,User,SolicitudesCliente
from django.contrib import messages
from django.core.mail import send_mail

from django.http import HttpResponse

 


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
        try:
            detalle_usuario = Admin.objects.get(correo=request.POST['correo'], contrasena_admin=request.POST['contrasena_admin'])
            request.session['correo'] = detalle_usuario.correo
            return render(request, 'logeado_ad.html')
        except Admin.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos.')
    return render(request, 'logins/login_ad.html')

def cerrar_session(request):
    try:
        del request.session['correo']
    except KeyError:
        pass
    return render(request, 'layouts/app.html')




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



def especializaciones(request, type_id):
    # Filtrar los objetos de Coach por typo_id
    especializaciones = Coach.objects.filter(typo_id=type_id)

    # Renderizar la plantilla con los objetos filtrados
    return render(request, 'views_especializaion/especializaciones.html', {'especializaciones': especializaciones})


def ad_coach(request, type_id):
    # Filtrar los objetos de Coach por typo_id
    especializaciones = Coach.objects.filter(typo_id=type_id)
    # Renderizar la plantilla con los objetos filtrados
    return render(request, 'views_ad/ad_coach.html', {'especializaciones': especializaciones})

def ad_user(request):
    # Obtener todos los usuarios
    users = User.objects.all()
    return render(request, 'profile/ad_user.html', {'users': users})

def user_detail(request, user_id):
    # Obtener el usuario específico o devolver 404 si no existe
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile/user_detail.html', {'user': user})


def especializacion_detalle(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
 # Define user como None, ya que no está disponible en esta vista
    return render(request, 'views_especializaion/especializacion_detalle.html', {'coach': coach})


def eliminar_detalle(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
 # Define user como None, ya que no está disponible en esta vista
    coaches = Coach.objects.all()
    return render(request, 'views_ad/eliminar_detalle.html', {'coach': coach})




def inscribir_user(request):
    if request.method == 'POST':
        form = SolicitudesClienteForm(request.POST)
        if form.is_valid():
            form.save()

            # Obtener los datos del usuario
            documento = request.POST.get('documento')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            # Obtener otros campos del usuario de manera similar

            # Enviar correo electrónico con los datos del usuario y del formulario
            subject = 'Nueva solicitud de cliente'
            message = f'Solicitud de cliente:\n\nDocumento: {documento}\nNombre: {nombre}\nApellido: {apellido}\n\n{form.cleaned_data}'
            sender_email = 'dojigo555@gmail.com'
            recipient_list = ['dojigo555@gmail.com', 'otracorreo@email.com']
            send_mail(subject, message, sender_email, recipient_list)

            messages.success(request, 'Tu solicitud ha sido enviada correctamente.')
            return redirect('logeado_cl')  # Redirige a la página de perfil del coach o a donde necesites
        else:
            messages.error(request, 'Hubo un error al procesar tu solicitud. Por favor, inténtalo de nuevo.')
    else:
        form = SolicitudesClienteForm()
        return render(request,'views_especializaion/inscripciones.html', {'form': form} )
    






def buscar_user_view(request):
    show_inscripcion_form = False
    
    if request.method == 'POST':
        documento = request.POST.get('documento')
        user = Coach.objects.filter(documento=documento).first()

        if user:
            show_inscripcion_form = True
            return render(request, 'views_especializaion/inscripciones.html', {'user': user, 'show_inscripcion_form': show_inscripcion_form})
        else:
            messages.error(request, 'No se encontró ningún coach con el documento proporcionado.')
            return render(request, 'views_especializaion/inscripciones.html', {'show_inscripcion_form': show_inscripcion_form})
    else:
        return render(request, 'views_especializaion/inscripciones.html', {'show_inscripcion_form': show_inscripcion_form})





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
        try:
            user = User.objects.get(documento=documento)
            print('no existe')
            return render(request, 'profile/profile_cl.html', {'user': user})
        except User.DoesNotExist:
            
            messages.error(request, 'No se encontró ningún usuario con el documento proporcionado.')
            return redirect('buscar_user')
    else:
        # Proporcionar un contexto con un diccionario vacío cuando no se haya enviado ningún formulario
        return render(request, 'profile/profile_cl.html', {})





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

def ingresar_user(request):
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

