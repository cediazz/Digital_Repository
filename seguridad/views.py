from django.contrib import messages
from .forms import UserLoginForm,UserPasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'Password/Password.html'
    

    