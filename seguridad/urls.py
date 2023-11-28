from django.contrib import admin
from django.urls import path
from .views import Authenticate

urlpatterns = [
    path('Authenticate/', Authenticate.as_view()),
]