from django.contrib.auth.views import LoginView
from ..forms import UserLoginForm

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'
