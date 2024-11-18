from django.views.generic import  UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Document
from ..forms import DocumentForm


class DocumentUpdateView(LoginRequiredMixin,UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'UpdateDocument/UpdateDocument.html'
    context_object_name = 'document'
    
    
    def get_success_url(self):
        return reverse_lazy('document-update', kwargs={'pk': self.object.pk})
        
