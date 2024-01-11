from django.utils.decorators import method_decorator
from ..Utils import admin_restriction
from django.views.generic import CreateView
from ..forms import UserCreateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..models import MyUser


@method_decorator(admin_restriction, name='dispatch')
class UserCreateView(CreateView):
    model = MyUser
    form_class = UserCreateForm
    template_name = 'InsertUser/InsertUser.html'
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('home')  
        return render(self.request, self.template_name, {'form': form})