from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Validar que solo se suban documentos en PDF
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    if ext.lower() != '.pdf':
        raise ValidationError(_('Solo se permiten archivos en formato PDF.'))