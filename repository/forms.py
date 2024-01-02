from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta():
        model = Document
        fields = ['title','description','author','theme','file']
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),max_length=255)
        self.fields['description'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'description'}))
        self.fields['author'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'author'}),max_length=255)
        self.fields['theme'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'theme'}),max_length=255)
        self.fields['file'] = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'file'}))