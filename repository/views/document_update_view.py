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
        """Al utilizar reverse_lazy(), se pospone la resolución de la URL hasta que sea necesaria, 
           lo que puede ser útil en este contexto. Esto significa que la URL no se resolverá 
           inmediatamente cuando se defina la vista, sino que se resolverá cuando sea necesario, por 
           ejemplo, después de que el usuario actualice un documento y se requiera redirigirlo a la 
           página de actualizacion del documento.El método reverse_lazy, en este caso, devolverá la 
           URL respectiva para la vista 'document-update' con el parámetro 'pk' del objeto actual."""