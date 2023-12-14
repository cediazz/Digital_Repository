from .forms import UserLoginForm,UserPasswordChangeForm,UserUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'Password/Password.html'

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'Password/PasswordDone.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "¡Tu contraseña ha sido cambiada con éxito!"
        return context

class UserUpdateView(View):
    template_name = 'Profile/Profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name,{'form': form})
    

    