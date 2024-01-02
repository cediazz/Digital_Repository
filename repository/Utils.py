from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import fitz
from repo_tourism.settings import MEDIA_ROOT


#Validar que solo se suban documentos en PDF
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    if ext.lower() != '.pdf':
        raise ValidationError(_('Solo se permiten archivos en formato PDF.'))

# Extraer y salvar imagen de la primera pagina del PDF
def save_image_pdf(file_name, pdf_file_path):
    try:
         pdf_document = fitz.open(pdf_file_path) # Leer el documento
         primera_pagina = pdf_document.load_page(0) # Extraer la imagen de la primera página del documento PDF
         pix = primera_pagina.get_pixmap() # Obtener una imagen de la primera pagina del documento
         pix.save(f"{MEDIA_ROOT}\Documents\{file_name}.png") # salvar la imagen en la carpeta designada para guardar los ficheros
        
    except Exception as e:
         print("Error al procesar el archivo PDF:", e)