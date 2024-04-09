
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('index/list/coachs/fitness/', views.list_coachs_fitness, name='list_coachs_fitness'),
    path('detalle/entrenador/fitness/<int:coach_id>/', views.detalle_coachs_fitness, name='detalle_coachs_fitness'),
    path('signup_opcion/index/',views.signup_opcion,name='signup_opcion'),
    path('login_opcion/index/',views.login_opcion,name='login_opcion'),
    path('signup_opcion/signup/ad/',views.signup_ad,name='signup_ad'),
    path('signup_opcion/signup/cl/',views.signup_cl,name='signup_cl'),
    path('signup_opcion/signup/en/', views.signup_en, name='signup_en'),

    path('login_ad/login_opcion/', views.login_ad, name='login_ad'),
    path('login_en/login_opcion/', views.login_en, name='login_en'),
    path('login_cl/login_opcion/', views.login_cl, name='login_cl'),
    path('logeado_ad/', views.logeado_ad, name='logeado_ad'), 
    path('logeado_en/', views.logeado_en, name='logeado_en'), 
    path('logeado_cl/', views.logeado_cl, name='logeado_cl'),
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('inscribirse_clase/', views.inscribirse_clase, name='inscribirse_clase'),
    path('dietas/', views.dietas, name='dietas'),
    path('vista_ampliada/', views.vista_ampliada, name='vista_ampliada'),




   
]

    # path('listar_paises/', views.listar_paises, name="listar_paises"),

    # path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),

    # path('editar_pais/<int:pais_id>/', views.editar_pais, name="editar_pais"),

    # path('recuperar_pais/', views.recuperar_pais, name="recuperar_pais"),
    
    # path('eliminar_pais/', views.eliminar_pais, name="eliminar_pais"),



 # path('login_cl/login_opcion', views.login_cl, name='login_cl'),
