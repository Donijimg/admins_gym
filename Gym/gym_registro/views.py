from django.shortcuts import render
from .form_signup import SignupAdminPartOne, SignupAdminPartTwo
from .models import AdminOficial,Entrenador,InscripcionCliente

def signup_ad(request):
    if request.method == 'POST':
        admin_part_one = SignupAdminPartOne(request.POST)
        admin_part_two = SignupAdminPartTwo(request.POST)
        if admin_part_one.is_valid() and admin_part_two.is_valid():
            # Procesa los datos del formulario y guarda el administrador
            identificacion_propietario = admin_part_one.cleaned_data['DNI_propietario']
            documento = admin_part_one.cleaned_data['Documento']
            nombre_admin = admin_part_one.cleaned_data['Nombre_admin']
            apellido_admin = admin_part_one.cleaned_data['Apellido_admin']
            telefono = admin_part_two.cleaned_data['telefono']
            correo = admin_part_two.cleaned_data['correo']
            direccion = admin_part_two.cleaned_data['direccion']
            contrasena_admin = admin_part_two.cleaned_data['contrasena_admin']
            
            # Guarda el administrador en la base de datos
            admin_save = AdminOficial.objects.create(
                identificacion_propietario=identificacion_propietario,
                documento=documento,
                nombre_admin=nombre_admin,
                apellido_admin=apellido_admin,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                contrasena_admin=contrasena_admin
            )
            
            return render(request, 'bienvenido.html', {'admin_save': admin_save})
    else:
        admin_part_one = SignupAdminPartOne()
        admin_part_two = SignupAdminPartTwo()
    
    return render(request, 'signup_administrador.html', {'admin_part_one': admin_part_one, 'admin_part_two': admin_part_two})


def index(request):
    return render(request, 'index.html', {})

def index_logeado(request):
    return render(request, 'index_logeado.html', {})


def signup_opcion(request):
    return render(request, 'signup_opcion.html', {})

def login_opcion(request):
    return render(request, 'login_opcion.html', {})


# def signup_ad(request):
#      if request.method == 'POST':
#          return save_admin(request)
#      else:
#          nuevo_admin = AdminOficial.objects.all()
#          return render(request, 'signup_administrador.html', {'nuevo_admin': nuevo_admin})
     

# def save_admin(request):
#   identificacion_propietario = request.POST.get('identificacion_propietario')
#   documento = request.POST.get('documento')
#   nombre_admin = request.POST.get('nombre_admin')
#   apellido_admin  = request.POST.get('apellido_admin')
#   telefono = request.POST.get('telefono')
#   correo = request.POST.get('correo')
#   direccion = request.POST.get('direccion')
#   contrasena_admin = request.POST.get('contrasena_admin')
 
 
#   admin_guardado = AdminOficial.objects.create(identificacion_propietario=identificacion_propietario,documento=documento,nombre_admin=nombre_admin,
#   apellido_admin=apellido_admin,telefono=telefono,correo=correo,direccion=direccion,contrasena_admin=contrasena_admin)
#   return render(request, 'bienvenido.html', {'admin_guardado': admin_guardado})




def signup_en(request):
  if request.method == 'POST':
    return save_entrenador(request)
  return render(request, 'signup_entrenador.html', {})

def save_entrenador(request):
  ficha_de_ingreso = request.POST.get('ficha_de_ingreso')
  documento = request.POST.get('documento')
  nombre = request.POST.get('nombre')
  apellido = request.POST.get('apellido')
  fecha_nacimiento = request.POST.get('fecha_nacimiento')
  telefono = request.POST.get('telefono')
  correo = request.POST.get('correo')
  direccion = request.POST.get('direccion')
  experiencia = request.POST.get('experiencia')
  conocimiento = request.POST.get('conocimiento')

  entrenador_guardado =Entrenador.objects.create(ficha_de_ingreso=ficha_de_ingreso,documento=documento,nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento,telefono=telefono,correo=correo,direccion=direccion,experiencia=experiencia,conocimiento=conocimiento)
  return render(request, 'bienvenido.html', {'entrenador_guardado':entrenador_guardado})

# entrenadores_con_mismo_nombre = Entrenador.objects.filter(nombre_usuario=nombre_usuario)
#     if entrenadores_con_mismo_nombre.exists():
#         # Informar al usuario que el nombre de usuario ya está en uso
#         return render(request, 'signup_entrenador.html', {'error_message': 'El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario.'})





def signup_cl(request):
    if request.method == 'POST':
        return save_cliente(request)
    return render(request, 'signup_cliente.html', {})

def save_cliente(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    edad = request.POST.get('edad')
    genero = request.POST.get('genero')
    telefono = request.POST.get('telefono')
    contrasena = request.POST.get('contrasena')

    nuevo_cliente = InscripcionCliente.objects.create(nombre=nombre, apellido=apellido, edad=edad, genero=genero, telefono=telefono, contrasena=contrasena)
    return render(request, 'bienvenido.html', {'nuevo_cliente': nuevo_cliente})





def login_ad(request):
    if request.method == 'POST':
        identificacion_propietario = request.POST.get('identificacion_propietario')
        contrasena_admin = request.POST.get('contrasena_admin')

        # Verificar las credenciales del administrador
        try:
            admin = AdminOficial.objects.get(identificacion_propietario=identificacion_propietario, contrasena_admin=contrasena_admin)
            # Si las credenciales son válidas, se puede redirigir o mostrar un mensaje de éxito
            return render(request, 'bienvenido.html')
        except AdminOficial.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'login_administrador.html', {'error': True})

    return render(request, 'login_administrador.html', {})


def login_en(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del entrenador
        try:
            entrenador = Entrenador.objects.get(documento=documento, contrasena=contrasena)
            # Si las credenciales son válidas, renderizar la página de bienvenida
            return render(request, 'bienvenido.html')
        except Entrenador.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'login_entrenador.html', {'error': True})

    return render(request, 'login_entrenador.html', {})

def login_en(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del entrenador
        try:
            entrenador = Entrenador.objects.get(documento=documento, contrasena=contrasena)
            # Si las credenciales son válidas, renderizar la página de bienvenida
            return render(request, 'bienvenido.html')
        except Entrenador.DoesNotExist:
            # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
            return render(request, 'login_entrenador.html', {'error': True})

    return render(request, 'login_entrenador.html', {})





# def login_cl(request):
#     if request.method == 'POST':
#         nombre_usuario = request.POST.get('nombre_usuario')
#         contrasena = request.POST.get('contrasena')

#         # Verificar las credenciales del cliente
#         try:
#             cliente = InscripcionCliente.objects.get(nombre_usuario=nombre_usuario, contrasena=contrasena)
#             # Si las credenciales son válidas, se puede redirigir o mostrar un mensaje de éxito
#             return render(request, 'bienvenido.html')
#         except InscripcionCliente.DoesNotExist:
#             # Si las credenciales son inválidas, puedes mostrar un mensaje de error o renderizar nuevamente el formulario de inicio de sesión
#             return render(request, 'login_cliente.html', {'error': True})

#     return render(request, 'login_cliente.html', {})




# def editar_entrenador(request, entrenador_id):
#     try:
#         entrenador = Entrenador.objects.get(id=entrenador_id)
#     except Entrenador.DoesNotExist:
#         return HttpResponse("El entrenador que intentas editar no existe.")

#     if request.method == 'POST':
#         return save_entrenador(request, entrenador)
#     else:
#         return render(request, 'editar_entrenador.html', {'entrenador': entrenador})


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






# views del del admin total

# def signup_ad(request):


  
    

# def listar_entrenadores_admin(request):
#     filtro_nombre= request.GET.get('nombre_campo')
#     repite lo mismo para los demas campos

#     objeto = modelo.objects.all()
# llama las tablas para poder acceder a sus datos 

#     if filtro_nombre:
#         objeto = objeto.filter(nombre_campo__icontains=filtro_nombre)

#     return render(request, 'listar_modelo.html', {'objeto': objeto, })
#     def tabla_modelo(request):

# def listar_clientes_admin(request):
#     filtro_nombre= request.GET.get('nombre_campo')
#     repite lo mismo para los demas campos

#     objeto = modelo.objects.all()
# llama las tablas para poder acceder a sus datos 

#     if filtro_nombre:
#         objeto = objeto.filter(nombre_campo__icontains=filtro_nombre)

#     return render(request, 'listar_modelo.html', {'objeto': objeto, })
#     def tabla_modelo(request):

# def tabla_modelo(request):
#     return render(request, 'tabla_modelo.html', {})

# def recuperar_modelo(request):
#     objeto_id = request.GET['id']
#     objeto = modelo.objects.get(id=objeto_id)
#     save_modelo(objeto)
#     return render(request, 'recuperar_modelo.html', {'objeto': objeto})

# def eliminar_modelo(request):
#     objeto_id = request.GET['id']
#     objeto=modelo.objects.get(id=objeto_id).delete()
#     save_modelo(pais)
#     return render(request, 'eliminar_modelo.html',{'objeto': objeto})


# #login y sing up del entrenador 



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
