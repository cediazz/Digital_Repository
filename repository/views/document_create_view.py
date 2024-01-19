from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from ..forms import DocumentForm
import os.path
from ..Utils import save_image_pdf
from django.shortcuts import render
from django.utils.decorators import method_decorator
from security.Utils import admin_restriction
from Digital_Repository. settings import MEDIA_ROOT
@method_decorator(admin_restriction, name='dispatch')
class DocumentCreateView(LoginRequiredMixin,CreateView):
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
