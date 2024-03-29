from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import fitz
from Digital_Repository.settings import MEDIA_ROOT
import os
from django.core.exceptions import ValidationError

#Validar que solo se suban documentos en PDF
def validate_file_extension(value):
    
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    if ext.lower() != '.pdf':
        raise ValidationError(_('Solo se permiten archivos en formato PDF.'))

# Extraer y salvar imagen de la primera pagina del PDF
def save_image_pdf(file_name, pdf_file_path):
    try:
         pdf_document = fitz.open(pdf_file_path) # Leer el documento
         primera_pagina = pdf_document.load_page(0) # Extraer la primera página del documento PDF
         pix = primera_pagina.get_pixmap() # Obtener una imagen de la primera pagina del documento
         pdf_path = os.path.join(MEDIA_ROOT, 'Documents') #Utilizamos os.path.join para construir la ruta de forma compatible con cualquier so
         image_path = os.path.join(pdf_path, f"{file_name}.png")
         pix.save(image_path) # salvar la imagen en la carpeta designada para guardar los ficheros
    except Exception as e:
          raise ValidationError(_(f'Ocurrió algun error procesando el documento PDF: {e}'))