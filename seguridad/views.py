from .forms import UserLoginForm,UserPasswordChangeForm,UserUpdateForm,UserCreateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Sign-in/sign-in.html'
    extra_context = {'message':'','form':form_class}

    def form_valid(self, form):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            # Si el usuario autenticado es un administrador, redirige a la página de inicio
            self.extra_context['message'] = 'No se puede acceder en estos momentos, se esta trabajando en la administración del sistema'
            return render(self.request,self.template_name, self.extra_context)
        # Si el usuario autenticado no es un administrador, permite que la vista de inicio de sesión se ejecute normalmente
        self.extra_context['message'] = ''
        return super().form_valid(form)

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
    
    def post(self, request):
       form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
       if form.is_valid():
            form.save()
            return redirect('profile')  
       return render(request, self.template_name, {'form': form})


class UserCreateView(View):
    template_name = 'InsertUser/InsertUser.html'

    def get(self, request):
        form = UserCreateForm()
        return render(request, self.template_name,{'form': form})
    
    def post(self, request):
       form = UserCreateForm(request.POST, request.FILES)
       print(request.FILES)
       if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
       return render(request, self.template_name, {'form': form})
    

    