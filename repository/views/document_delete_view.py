from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DeleteView
from ..models import Document
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from security.Utils import admin_restriction
@method_decorator(admin_restriction, name='dispatch')
class DocumentDeleteView(LoginRequiredMixin,DeleteView):
    model = Document
    success_url = reverse_lazy('documents-byuser') #definir la URL a la que se redirigirá el usuario después de eliminar exitosamente un documento
    """Al utilizar reverse_lazy(), se pospone la resolución de la URL hasta que sea necesaria, 
    lo que puede ser útil en este contexto. Esto significa que la URL no se resolverá 
    inmediatamente cuando se defina la vista, sino que se resolverá cuando sea necesario, por 
    ejemplo, después de que el usuario elimine un documento y se requiera redirigirlo a la 
    página de documentos del usuario""" 