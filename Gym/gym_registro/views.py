from django.shortcuts import render
from django.http import HttpResponse
from .models import Entrenador,InscripcionCliente,RutinaCliente

def index(request):
    return render(request, 'index.html', {})

#login y sing up del entrenador 

def registrar_entrenador(request):
    if request.method == 'POST':
        # Si el método de solicitud es POST, guarda el entrenador
        return save_entrenador(request)
    else:
        # Si el método de solicitud es GET, muestra el formulario de registro
        entrenadores = Entrenador.objects.all()
        return render(request, 'registrar_entrenador.html', {'entrenadores': entrenadores})

def save_entrenador(request, entrenador=None):
    if request.method == 'POST':
        # Procesa los datos del formulario
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

        if entrenador is None:
            # Si no se proporciona un entrenador existente, se crea uno nuevo
            nuevo_entrenador = Entrenador.objects.create(
                ficha_de_ingreso=ficha_de_ingreso,
                documento=documento,
                nombre=nombre,
                apellido=apellido,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                anos_de_experiencia=anos_de_experiencia,
                conocimiento=conocimiento,
                horario_de_entrada=horario_de_entrada,
                horario_de_salida=horario_de_salida
            )

            return HttpResponse(f"Se registró el Entrenador {nuevo_entrenador}.")
        else:
            # Si se proporciona un entrenador existente, se actualizan sus datos
            entrenador.ficha_de_ingreso = ficha_de_ingreso
            entrenador.documento = documento
            entrenador.nombre = nombre
            entrenador.apellido = apellido
            entrenador.fecha_nacimiento = fecha_nacimiento
            entrenador.genero = genero
            entrenador.telefono = telefono
            entrenador.correo = correo
            entrenador.direccion = direccion
            entrenador.anos_de_experiencia = anos_de_experiencia
            entrenador.conocimiento = conocimiento
            entrenador.horario_de_entrada = horario_de_entrada
            entrenador.horario_de_salida = horario_de_salida
            save_entrenador(entrenador)

            return HttpResponse(f"Se actualizaron los datos del Entrenador {entrenador}.")

    return HttpResponse("El método de solicitud no es POST.")



def editar_entrenador(request, entrenador_id):
    try:
        entrenador = Entrenador.objects.get(id=entrenador_id)
    except Entrenador.DoesNotExist:
        return HttpResponse("El entrenador que intentas editar no existe.")

    if request.method == 'POST':
        return save_entrenador(request, entrenador)
    else:
        return render(request, 'editar_entrenador.html', {'entrenador': entrenador})


#views del del admin total

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
