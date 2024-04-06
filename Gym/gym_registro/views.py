from django.shortcuts import render
from django.http import HttpResponse
from .models import AdminOficial,Entrenador,InscripcionCliente,RutinaCliente

def index(request):
    return render(request, 'index.html', {})


def signup_opcion(request):
    return render(request, 'signup_opcion.html', {})

def login_opcion(request):
    return render(request, 'login_opcion.html', {})


def signup_ad(request):
     if request.method == 'POST':
         return save_admin(request)
     else:
         nuevo_admin = AdminOficial.objects.all()
         return render(request, 'signup_administrador.html', {'nuevo_admin': nuevo_admin})
     

def save_admin(request,):
  identificacion_propietario = request.POST.get('identificacion_propietario')
  documento = request.POST.get('documento')
  nombre_admin = request.POST.get('nombre_admin')
  apellido_admin  = request.POST.get('apellido_admin')
  telefono = request.POST.get('telefono')
  correo = request.POST.get('correo')
  direccion = request.POST.get('direccion')
  contrasena_admin = request.POST.get('contrasena_admin')
 
 
  admin_guardado = AdminOficial.objects.create(identificacion_propietario=identificacion_propietario,documento=documento,nombre_admin=nombre_admin,
  apellido_admin=apellido_admin,telefono=telefono,correo=correo,direccion=direccion,contrasena_admin=contrasena_admin)
  return render(request, 'bienvenido.html', {'admin_guardado': admin_guardado})




def signup_en(request):
  if request.method == 'POST':
    return save_entrenador(request)
  return render(request, 'signup_entrenador.html', {})

def save_entrenador(request,):
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



def signup_cl(request):
    return render(request, 'signup_cliente.html', {})


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
