
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('signup_opcion/',views.signup_opcion,name='signup_opcion'),
    # path('login_opcion/index',views.login_opcion,name='login_opcion')

    path('save_entrenador/signup_ad/', views.save_entrenador, name='save_entrenador'),
    path('save_admin/signup_ad/', views.save_admin, name='save_admin'), 
    path('signup_ad/signup_opcion/',views.signup_ad,name='signup_ad'),
    path('signup_cl/signup_opcion/',views.signup_cl,name='signup_cl'),
    path('signup_en/signup_opcion/', views.signup_en, name='signup_en'),

    

    # path('listar_paises/', views.listar_paises, name="listar_paises"),

    # path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),

    # path('editar_pais/<int:pais_id>/', views.editar_pais, name="editar_pais"),

    # path('recuperar_pais/', views.recuperar_pais, name="recuperar_pais"),
    
    # path('eliminar_pais/', views.eliminar_pais, name="eliminar_pais"),
]



