from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DeleteView
from ..models import Document
from django.urls import reverse_lazy


class DocumentDeleteView(LoginRequiredMixin,DeleteView):
    model = Document
    success_url = reverse_lazy('documents-byuser')
    
