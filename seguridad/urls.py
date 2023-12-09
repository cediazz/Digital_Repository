from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView,CustomPasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cambiar-contrasena/', auth_views.PasswordChangeView.as_view(template_name='Password/Password.html', success_url='cambiar-contrasena/'), name='cambiar-contrasena'),
    path('change-password/', CustomPasswordChangeView.as_view(success_url='/Seguridad/change-password/'), name='change-password'),
   ]