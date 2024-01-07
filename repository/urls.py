from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import DocumentCreateView,DocumentListViewByUser,DocumentDetailView,DocumentUpdateView,DocumentDeleteView,DocumentListViewByTheme


urlpatterns = [
   
    path('documents',DocumentCreateView.as_view(), name='documents'),
    path('document-detail/<int:pk>',DocumentDetailView.as_view(), name='document-detail'),
    path('documents-byuser',DocumentListViewByUser.as_view(), name='documents-byuser'),
    path('document-update/<int:pk>',DocumentUpdateView.as_view(), name='document-update'),
    path('document-delete/<int:pk>',DocumentDeleteView.as_view(), name='document-delete'),
    path('document-bytheme',DocumentListViewByTheme.as_view(), name='document-bytheme'),
    
   
]
