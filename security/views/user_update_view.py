from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from ..models import MyUser
from ..forms import UserUpdateForm
from django.urls import reverse_lazy


class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = MyUser
    form_class = UserUpdateForm
    template_name = 'Profile/Profile.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
