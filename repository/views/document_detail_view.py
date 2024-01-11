from django.views.generic import  DetailView
from ..models import Document
from django.utils.decorators import method_decorator
from seguridad.Utils import admin_restriction
@method_decorator(admin_restriction, name='dispatch')
class DocumentDetailView(DetailView):
    model = Document
    template_name = "DetailDocument/DetailDocument.html"
    context_object_name = 'document'