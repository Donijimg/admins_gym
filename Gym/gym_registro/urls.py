
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
  
  # path('cerrar_session/',views.cerrar_session, name='cerrar_session'),
  path('login_ad/login_opcion/', views.login, name='login_ad'),

  path('login_ad/', views.login_ad, name='login_ad'), 
  path('login_en/', views.login_en, name='login_en'), 
  path('login_cl/', views.login_cl, name='login_cl'), 
  
  path('buscar_login_ad/', views.buscar_login_ad, name='buscar_login_ad'),
  path('buscar_login_cl/', views.buscar_login_cl, name='buscar_login_cl'),
  path('buscar_login_en/', views.buscar_login_en, name='buscar_login_en'),
  
  path('coach_admin/<int:type_id>/', views.coach_admin, name='coach_admin'),
  path('detalle_coach/<int:coach_id>/', views.detalle_coach, name='detalle_coach'),
  
  path('logeado_ad/', views.logeado_ad, name='logeado_ad'), 
  path('logeado_en/', views.logeado_en, name='logeado_en'), 
  path('logeado_cl/', views.logeado_cl, name='logeado_cl'), 
  
  path('welcome_ad/', views.welcome_ad, name='welcome_ad'),
  path('welcome_en/', views.welcome_en, name='welcome_en'),
  path('welcome_cl/', views.welcome_cl, name='welcome_cl'),

  path('ad_coach/<int:type_id>/',views.ad_coach, name='ad_coach'),
  path('especializaciones/<int:type_id>/',views.especializaciones, name='especializaciones'),
  path('especializacion_detalle/<int:coach_id>/', views.especializacion_detalle, name='especializacion_detalle'),
  
  path('eliminar_detalle/<int:coach_id>/', views.eliminar_detalle, name='eliminar_detalle'),
  path('ad_user/', views.ad_user, name='ad_user'),
  path('ad_user/<int:user_id>/', views.user_detail, name='user_detail'),

  path('inscribir_user/', views.inscribir_user, name='inscribir_user'),
  path('buscar_user_view/', views.buscar_user_view, name='buscar_user_view'),

  #vistas para entrenadores 
  path('vista_dietas_fitness/', views.vista_dietas_fitness, name='vista_dietas_fitness'),
  path('vista_dietas_pilates/', views.vista_dietas_pilates, name='vista_dietas_pilates'),
  path('vista_dietas_rehabilitacion/', views.vista_dietas_rehabilitacion, name='vista_dietas_rehabilitacion'),
  path('vista_dietas_mayores/', views.vista_dietas_mayores, name='vista_dietas_mayores'),  
  path('vista_dietas_yoga/', views.vista_dietas_yoga, name='vista_dietas_yoga'),  
  path('vista_dietas_gimnasia/', views.vista_dietas_gimnasia, name='vista_dietas_gimnasia'),  
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
    
  path('eliminar_entrenador_por_documento/', views.eliminar_entrenador_por_documento, name='eliminar_entrenador_por_documento'),
  path('eliminar_cuenta_por_documento/', views.eliminar_cuenta_por_documento, name='eliminar_cuenta_por_documento'),
  #mostar
  path('acercade/', views.acercade, name='acercade'),
  path('profile_ad/', views.profile_ad, name='profile_ad'),
  path('profile_en/', views.profile_en, name='profile_en'),
  path('profile_cl/', views.profile_cl, name='profile_cl'),
  
  path('galeria/', views.galeria, name='galeria'),


]


