from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView,CustomPasswordChangeView,CustomPasswordChangeDoneView,UserUpdateView,UserCreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('done-password/', CustomPasswordChangeDoneView.as_view(),name='done-password'),
    path('change-password/', CustomPasswordChangeView.as_view(success_url='/Seguridad/done-password/'),name='change-password'),
    path('profile/',UserUpdateView.as_view(),name='profile'),
    path('insert-user/',UserCreateView.as_view(),name='insert-user'),
   ]