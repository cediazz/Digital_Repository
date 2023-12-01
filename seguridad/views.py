from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'

    def form_invalid(self, form):
        # Personalizar el comportamiento cuando la autenticación falla
        # Por ejemplo, puedes definir un mensaje de error personalizado
        error_message = "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."

        # Puedes agregar el mensaje de error al formulario
        form.add_error(None, error_message)
       
        # Redirigir al usuario de vuelta al formulario de inicio de sesión con el mensaje de error.
        return super().form_invalid(form)