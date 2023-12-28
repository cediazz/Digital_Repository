from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import DocumentCreateView


urlpatterns = [
   
    path('documents',DocumentCreateView.as_view(), name='documents'),
   
]
