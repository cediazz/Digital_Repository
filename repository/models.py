from django.db import models
from security.models import MyUser
from.Utils import validate_file_extension
import os

class Document(models.Model):
    title = models.CharField(max_length=255,unique=True,verbose_name='título')
    description = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    file = models.FileField(upload_to='Documents/', blank=False, validators=[validate_file_extension])
    image = models.ImageField(upload_to='Documents/')
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "documento"
    
    #Eliminar el documento fisicamente en el sistema de archivos
    def delete(self, *args, **kwargs):
        # Eliminar el archivo asociado
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        # Llamar al método delete original par eliminar el registro del documento en la BD
        super(Document, self).delete(*args, **kwargs)



