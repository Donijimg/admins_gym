
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('registrar_entrenador/', views.registrar_entrenador, name='registrar_entrenador'),
    path('save_entrenador/', views.save_entrenador, name='save_entrenador'),  # URL para save_entrenador

    # path('listar_paises/', views.listar_paises, name="listar_paises"),

    # path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),

    # path('editar_pais/<int:pais_id>/', views.editar_pais, name="editar_pais"),

    # path('recuperar_pais/', views.recuperar_pais, name="recuperar_pais"),
    
    # path('eliminar_pais/', views.eliminar_pais, name="eliminar_pais"),
]



