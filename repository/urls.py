from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views.document_delete_view import DocumentDeleteView
from .views.document_update_view import DocumentUpdateView
from .views.document_create_view import DocumentCreateView
from .views.document_detail_view import DocumentDetailView
from .views.document_list_view import DocumentListViewByUser,DocumentListViewByTheme,DocumentListViewByAuthor

urlpatterns = [
   
    path('documents',DocumentCreateView.as_view(), name='documents'),
    path('document-detail/<int:pk>',DocumentDetailView.as_view(), name='document-detail'),
    path('documents-byuser',DocumentListViewByUser.as_view(), name='documents-byuser'),
    path('document-update/<int:pk>',DocumentUpdateView.as_view(), name='document-update'),
    path('document-delete/<int:pk>',DocumentDeleteView.as_view(), name='document-delete'),
    path('document-bytheme',DocumentListViewByTheme.as_view(), name='document-bytheme'),
    path('document-byauthor',DocumentListViewByAuthor.as_view(), name='document-byauthor'),
   
]
