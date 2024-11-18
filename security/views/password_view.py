from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from ..forms import UserPasswordChangeForm
from django.urls import reverse_lazy


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'Password/Password.html'
    
    
    def get_success_url(self):
        return reverse_lazy('done-password')


class CustomPasswordChangeDoneView(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'Password/PasswordDone.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "¡Tu contraseña ha sido cambiada con éxito!"
        return context
