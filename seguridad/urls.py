from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   ]