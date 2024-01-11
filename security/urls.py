from django.contrib import admin
from django.urls import path, include
from .views.login_view import CustomLoginView
from .views.password_view import CustomPasswordChangeDoneView,CustomPasswordChangeView
from .views.user_update_view import UserUpdateView
from .views.user_create_view import UserCreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('done-password/', CustomPasswordChangeDoneView.as_view(),name='done-password'),
    path('change-password/', CustomPasswordChangeView.as_view(),name='change-password'),
    path('profile/<int:pk>',UserUpdateView.as_view(),name='profile'),
    path('insert-user/',UserCreateView.as_view(),name='insert-user'),
   ]