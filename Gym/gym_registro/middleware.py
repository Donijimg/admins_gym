from django.shortcuts import redirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            # Si el usuario no está autenticado, redirigirlo a la página de inicio de sesión general
            return redirect('index')  # Reemplaza 'login' con el nombre de tu vista de inicio de sesión general

        # Verificar el rol del usuario y redirigir según corresponda
        if request.user.is_authenticated and request.user.is_cliente:
            # Si el usuario es un cliente, redirigir a la página de inicio de sesión de cliente
            return redirect('login_cl')  # Reemplaza 'login_cl' con el nombre de tu vista de inicio de sesión de cliente
        elif request.user.is_authenticated and request.user.is_administrador:
            # Si el usuario es un administrador, redirigir a la página de inicio de sesión de administrador
            return redirect('login_ad')  # Reemplaza 'login_ad' con el nombre de tu vista de inicio de sesión de administrador
        elif request.user.is_authenticated and request.user.is_entrenador:
            # Si el usuario es un entrenador, redirigir a la página de inicio de sesión de entrenador
            return redirect('login_en')  # Reemplaza 'login_en' con el nombre de tu vista de inicio de sesión de entrenador

        # Llamar al siguiente middleware en la cadena
        response = self.get_response(request)
        return response
