from .forms import UserLoginForm,UserPasswordChangeForm,UserUpdateForm,UserCreateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .Utils import admin_restriction
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(admin_restriction, name='dispatch')
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'
    


@method_decorator(admin_restriction, name='dispatch')
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'Password/Password.html'


@method_decorator(admin_restriction, name='dispatch')
class CustomPasswordChangeDoneView(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'Password/PasswordDone.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "¡Tu contraseña ha sido cambiada con éxito!"
        return context


@method_decorator(admin_restriction, name='dispatch')
class UserUpdateView(LoginRequiredMixin,View):
    template_name = 'Profile/Profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name,{'form': form})
    
    def post(self, request):
       form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
       if form.is_valid():
            form.save()
            return redirect('profile')  
       return render(request, self.template_name, {'form': form})


@method_decorator(admin_restriction, name='dispatch')
class UserCreateView(View):
    template_name = 'InsertUser/InsertUser.html'

    def get(self, request):
        form = UserCreateForm()
        return render(request, self.template_name,{'form': form})
    
    def post(self, request):
       form = UserCreateForm(request.POST, request.FILES)
       if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
       return render(request, self.template_name, {'form': form})
    

    