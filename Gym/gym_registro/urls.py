
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('signup_opcion/index/',views.signup_opcion,name='signup_opcion'),
    path('login_opcion/index/',views.login_opcion,name='login_opcion'),
    path('save_cliente/signup_cl/', views.save_cliente, name='save_cliente'),
    path('save_entrenador/signup_en/', views.save_entrenador, name='save_entrenador'),
    path('save_admin/signup_ad/', views.save_admin, name='save_admin'), 
    path('signup_ad/signup_opcion/',views.signup_ad,name='signup_ad'),
    path('signup_cl/signup_opcion/',views.signup_cl,name='signup_cl'),
    path('signup_en/signup_opcion/', views.signup_en, name='signup_en'),
    path('login_ad/login_opcion/', views.login_ad, name='login_ad'),
    path('login_en/login_opcion/', views.login_en, name='login_en'),
    path('index_logeado/', views.index_logeado, name='index_logeado'), 

   
]

    # path('listar_paises/', views.listar_paises, name="listar_paises"),

    # path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),

    # path('editar_pais/<int:pais_id>/', views.editar_pais, name="editar_pais"),

    # path('recuperar_pais/', views.recuperar_pais, name="recuperar_pais"),
    
    # path('eliminar_pais/', views.eliminar_pais, name="eliminar_pais"),



 # path('login_cl/login_opcion', views.login_cl, name='login_cl'),
