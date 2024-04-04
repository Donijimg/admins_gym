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
         # Si el método de solicitud es POST, guarda el entrenador
         return save_admin(request)
     else:
         # Si el método de solicitud es GET, muestra el formulario de registro
         administradores = AdminOficial.objects.all()
         return render(request, 'signup_administrador.html', {'administradores': administradores})
     

def save_admin(request,):
  DNI_propietario = request.POST.get('identificacion_propietario')
  documento = request.POST.get('documento')
  nombre_admin = request.POST.get('nombre_admin')
  nombre_apellido = request.POST.get('apellido')
  telefono = request.POST.get('telefono')
  correo = request.POST.get('correo')
  direccion = request.POST.get('direccion')
  contrasena = request.POST.get('contrasena_admin')
 
 
  nuevo_entrenador = Entrenador.objects.create(DNI_propietario=DNI_propietario,documento=documento,nombre_admin=nombre_admin,
  nombre_apellido=nombre_apellido,telefono=telefono,correo=correo,direccion=direccion,contrasena=contrasena,)
  return HttpResponse(f"Se registró el Entrenador {nuevo_entrenador}.")






    


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
  genero = request.POST.get('genero')
  telefono = request.POST.get('telefono')
  correo = request.POST.get('correo')
  direccion = request.POST.get('direccion')
  anos_de_experiencia = request.POST.get('anos_de_experiencia')
  conocimiento = request.POST.get('conocimiento')
  horario_de_entrada = request.POST.get('horario_de_entrada')
  horario_de_salida = request.POST.get('horario_de_salida')
  nuevo_entrenador = Entrenador.objects.create(ficha_de_ingreso=ficha_de_ingreso,documento=documento,nombre=nombre,
  apellido=apellido,fecha_nacimiento=fecha_nacimiento,genero=genero,telefono=telefono,correo=correo,direccion=direccion,
  anos_de_experiencia=anos_de_experiencia,conocimiento=conocimiento,horario_de_entrada=horario_de_entrada,
  horario_de_salida=horario_de_salida)
  return HttpResponse(f"Se registró el Entrenador {nuevo_entrenador}.")



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
