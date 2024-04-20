
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("gym_registro.urls")),
    path('accounts/', include('django.contrib.auth.urls')),  # Utiliza las vistas de autenticación predeterminadas de Django
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Ruta para iniciar sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
      
      

  # Ruta para cerrar sesión
]