
from django.urls import path
from . import views

urlpatterns = [





    path('', views.index, name="index"),

    
    # registro
    path('signup_opcion/index/',views.signup_opcion,name='signup_opcion'),
    path('login_opcion/index/',views.login_opcion,name='login_opcion'),
    
    path('signup_opcion/signup/ad/',views.signup_ad, name='signup_ad'),
    path('signup_opcion/signup/cl/',views.signup_cl,name='signup_cl'),
    path('signup_opcion/signup/en/',views.signup_en,name='signup_en'),
    
    path('login_ad/login_opcion/', views.login_ad, name='login_ad'),
    path('login_en/login_opcion/', views.login_en, name='login_en'),
    path('login_cl/login_opcion/', views.login_cl, name='login_cl'),
    
    path('logeado_ad/', views.logeado_ad, name='logeado_ad'), 
    path('logeado_en/', views.logeado_en, name='logeado_en'), 
    path('logeado_cl/', views.logeado_cl, name='logeado_cl'), 
    
    path('welcome_ad/', views.welcome_ad, name='welcome_ad'),
    path('welcome_en/', views.welcome_en, name='welcome_en'),
    path('welcome_cl/', views.welcome_cl, name='welcome_cl'),
    
   
    # path('inscribirse/<str:especializacion>/<int:id>/', views.inscribirse, name='inscribirse'),



    path('clientes_fitness/', views.list_clientes_fitness, name='list_clientes_fitness'),


    path('detalle_cliente_fitness/<int:inscripcion>/', views.detalle_cliente_fitness, name='detalle_cliente_fitness'),

  #vistas para admin
    path('admin_list_fitness/', views.list_all_fitness, name='list_all_fitness'),
    path('admin_list_pilates/', views.list_all_pilates, name='list_all_pilates'),
    path('admin_list_rehabilitacion/', views.list_all_rehabilitacion, name='list_all_rehabilitacion'),
    path('admin_list_mayores/', views.list_all_mayores, name='list_all_mayores'),
    path('admin_list_yoga/', views.list_all_yoga, name='list_all_yoga'),
    path('admin_list_gimnacia/', views.list_all_gimnacia, name='list_all_gimnacia'),



  #vistas para entrenadores 
    path('vista_dietas_fitness/', views.vista_dietas_fitness, name='vista_dietas_fitness'),
    path('vista_dietas_pilates/', views.vista_dietas_pilates, name='vista_dietas_pilates'),
    path('vista_dietas_rehabilitacion/', views.vista_dietas_rehabilitacion, name='vista_dietas_rehabilitacion'),
    path('vista_dietas_mayores/', views.vista_dietas_mayores, name='vista_dietas_mayores'),  
    path('vista_dietas_yoga/', views.vista_dietas_yoga, name='vista_dietas_yoga'),  
    path('vista_dietas_gimnasia/', views.vista_dietas_gimnasia, name='vista_dietas_gimnasia'),  


    path('regresar/<path:pagina_anterior>/', views.regresar, name='regresar'),


    path('mostrar_mensaje/<str:tipo>/', views.mostrar_mensaje, name='mostrar_mensaje'),




  


    path('buscar_admin/', views.buscar_admin, name='buscar_admin'),
    path('eliminar_admin/', views.eliminar_admin, name='eliminar_admin'),
    path('ingresar_admin/', views.ingresar_admin, name='ingresar_admin'),
    path('actualizar_admin/', views.actualizar_admin, name='actualizar_admin'),

    path('eliminar_coach/', views.eliminar_coach, name='eliminar_coach'),
    path('buscar_coach/', views.buscar_coach, name='buscar_coach'),
    path('ingresar_coach/', views.ingresar_coach, name='ingresar_coach'),
    path('actualizar_coach/', views.actualizar_coach, name='actualizar_coach'),

    path('eliminar_user/', views.eliminar_user, name='eliminar_user'),
    path('buscar_user/', views.buscar_user, name='buscar_user'),
    path('ingresar_user/', views.ingresar_user, name='ingresar_user'),
    path('actualizar_user/', views.actualizar_user, name='actualizar_user'),

      
  
    
    path('list_clientes_fitness/', views.list_clientes_fitness, name='list_clientes_fitness'),
    path('list_clientes_pilates/', views.list_clientes_pilates, name='list_clientes_pilates'),
    path('list_clientes_rehabilitacion/', views.list_clientes_rehabilitacion, name='list_clientes_rehabilitacion'),
    path('list_clientes_mayores/', views.list_clientes_mayores, name='list_clientes_mayores'),
    path('list_clientes_yoga/', views.list_clientes_yoga, name='list_clientes_yoga'),
    path('list_clientes_gimnacia/', views.list_clientes_fitness, name='list_clientes_gimnacia'),

    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),
    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),
    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),
    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),
    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),
    # path('detalle_inscripcion_fitness/<int:coach_id>/', views.detalle_inscripcion_fitness, name='detalle_inscripcion_fitness'),

  #vistas para clientes
    # path('index/list/coachs/fitness/', views.list_coachs_fitness, name='list_coachs_fitness'),
    # path('detalle/entrenador/fitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_fitness, name='detalle_coachs_fitness'),
          
    # path('index/list/coachs/rehabilitacion/', views.list_coachs_rehabilitacion, name='list_coachs_rehabilitacion'),
    # path('detalle/entrenador/rehabilitacionfitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_rehabilitacion, name='detalle_coachs_rehabilitacion'),


    # path('index/list/coachs/pilates/', views.list_coachs_pilates, name='list_coachs_pilates'),
    # path('detalle/entrenador/pilatesfitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_pilates, name='detalle_coachs_pilates'),


    # path('index/list/coachs/gimnasia/', views.list_coachs_gimnasia, name='list_coachs_gimnasia'),
    # path('detalle/entrenador/gimnasiafitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_gimnasia, name='detalle_coachs_gimnasia'),

    # path('index/list/coachs/yoga/', views.list_coachs_yoga, name='list_coachs_yoga'),
    # path('detalle/entrenador/yogafitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_yoga, name='detalle_coachs_yoga'),

    # path('index/list/coachs/mayores/', views.list_coachs_mayores, name='list_coachs_mayores'),
    # path('detalle/entrenador/mayoresfitness/<str:especialization>/<int:coach_id>/', views.detalle_coachs_mayores, name='detalle_coachs_mayores'),







    path('eliminar_entrenador_por_documento/', views.eliminar_entrenador_por_documento, name='eliminar_entrenador_por_documento'),
    path('eliminar_cuenta_por_documento/', views.eliminar_cuenta_por_documento, name='eliminar_cuenta_por_documento'),

    





    #mostar
    path('acercade/', views.acercade, name='acercade'),

    path('profile_ad/', views.profile_ad, name='profile_ad'),
    path('profile_en/', views.profile_en, name='profile_en'),
    path('profile_cl/', views.profile_cl, name='profile_cl'),
    
    path('galeria_one/', views.galeria_one, name='galeria_one'),
    path('galeria_two/', views.galeria_two, name='galeria_two'),
    path('galeria_three/', views.galeria_three, name='galeria_three'),
    path('galeria_four/', views.galeria_four, name='galeria_four'),
    path('galeria_five/', views.galeria_five, name='galeria_five'),

   
]


