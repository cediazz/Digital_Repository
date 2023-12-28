from django.shortcuts import render,redirect
from django.views import View 
from django.views.generic import ListView, CreateView
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class DocumentCreateView(CreateView):
    #model = Document
    form_class = DocumentForm
    template_name = 'Documents/Documents.html'  # Nombre del template que contendrá el formulario para crear un nuevo documento

    def form_valid(self, form):
        document = form.save(commit=False)
        document.user = self.request.user
        document.save()
        return render(self.request, self.template_name, {'form': form, 'message': 'Se guardó el documento exitosamente'})
