from django.db import models
from seguridad.models import MyUser
from.Utils import validate_file_extension

class Document(models.Model):
    title = models.CharField(max_length=255,unique=True,verbose_name='título')
    description = models.TextField()
    publication_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=255)
    key_words = models.CharField(max_length=255)
    file = models.FileField(upload_to='Documents/', blank=False, validators=[validate_file_extension])
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "documento"



