from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views import View 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Document
import os.path
from .Utils import save_image_pdf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
class DocumentListViewByUser(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'DocumentsByUser/DocumentsByUser.html'
    context_object_name = 'documents_paginated'
    items_per_page = 6

    def get_queryset(self):
        documents = Document.objects.filter(user=self.request.user).order_by('publication_date')
        # Paginar los resultados
        paginator = Paginator(documents, self.items_per_page)
        page_number = self.request.GET.get('page')
        documents_paginated = paginator.get_page(page_number)
        return documents_paginated


class DocumentDetailView(DetailView):
    model = Document
    template_name = "DetailDocument/DetailDocument.html"
    context_object_name = 'document'

@method_decorator(login_required, name='dispatch')
class DocumentCreateView(CreateView):
    #model = Document
    form_class = DocumentForm
    template_name = 'Documents/Documents.html'  # Nombre del template que contendrá el formulario para crear un nuevo documento

    def form_valid(self, form):
        document = form.save(commit=False)
        document.user = self.request.user
        # Guardar el documento en la base de datos
        document.save()
        file_name = os.path.basename(document.file.name)
        pdf_file_path = document.file.path # obtener la ruta donde se guardo el documento
        save_image_pdf(file_name, pdf_file_path) # Extraer y salvar imagen de la primera pagina del PDF
        document.image = f"Documents/{file_name}.png" # Asigna el archivo de imagen al campo 'image' de la instancia de Document
        document.save() # Guardar el documento actualizado con la imagen
        return render(self.request, self.template_name, {'form': form, 'message': 'Se guardó el documento exitosamente'})

@method_decorator(login_required, name='dispatch')
class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'UpdateDocument/UpdateDocument.html'
    context_object_name = 'document'
    
    def get_success_url(self):
        return reverse('document-update', kwargs={'pk': self.object.pk})
        """El método reverse en Django se utiliza para obtener la URL a partir del nombre de la vista y 
        los parámetros opcionales.El método reverse, en este caso, devolverá la URL respectiva para la 
        vista 'document-update' con el parámetro 'pk' del objeto actual."""
    

@method_decorator(login_required, name='dispatch')
class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'DocumentsByUser/DocumentsByUser.html'
    success_url = reverse_lazy('documents-byuser')
    
    
    
    