from django.utils.decorators import method_decorator
from ..Utils import admin_restriction
from django.contrib.auth.views import LoginView
from ..forms import UserLoginForm

@method_decorator(admin_restriction, name='dispatch')
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'