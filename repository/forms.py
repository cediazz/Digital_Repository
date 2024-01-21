from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta():
        model = Document
        fields = ['title','description','author','theme','file']
        widgets = {  # Se puede usar tambien la libreria django-widget-tweaks
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'description'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author'}),
            'theme': forms.TextInput(attrs={'class': 'form-control', 'id': 'theme'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'file'})
        }
   