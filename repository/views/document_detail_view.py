from django.views.generic import  DetailView
from ..models import Document

class DocumentDetailView(DetailView):
    model = Document
    template_name = "DetailDocument/DetailDocument.html"
    context_object_name = 'document'