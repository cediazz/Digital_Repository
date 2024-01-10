from django.views import View
from ..models import Document
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView 


class DocumentListViewByUser(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'DocumentsByUser/DocumentsByUser.html'
    context_object_name = 'documents_paginated'
    items_per_page = 6

    def get_queryset(self): # se ejecuta automaticamente al cargar la plantilla html
        documents = Document.objects.filter(user=self.request.user).order_by('-publication_date')
        # Paginar los resultados
        paginator = Paginator(documents, self.items_per_page)
        page_number = self.request.GET.get('page')
        documents_paginated = paginator.get_page(page_number)
        return documents_paginated



class DocumentListViewByTheme(View):
    
    items_per_page = 6

    def get(self, request):
        themes = Document.objects.values('theme').distinct().order_by('theme')
        documents_paginated = None
        if 'theme' in request.GET:
            documents = Document.objects.filter(theme = request.GET['theme'])
            paginator = Paginator(documents, self.items_per_page)
            page_number = self.request.GET.get('page')
            documents_paginated = paginator.get_page(page_number)
        return render(request,'DocumentsByTheme/DocumentsByTheme.html', {'themes': themes, 'documents_paginated': documents_paginated})
    

class DocumentListViewByAuthor(ListView):
    model = Document
    template_name = 'DocumentsByAuthor/DocumentsByAuthor.html'
    context_object_name = 'documents_paginated'
    items_per_page = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['documents_paginated']:
            context['message'] = "No se encontraron documentos"
        return context

    def get_queryset(self): # se ejecuta automaticamente al cargar la plantilla html
        documents = None
        if 'author' in self.request.GET:
           documents = Document.objects.filter(author = self.request.GET['author']).order_by('-publication_date')
        if documents != None:
           # Paginar los resultados
           paginator = Paginator(documents, self.items_per_page)
           page_number = self.request.GET.get('page')
           documents_paginated = paginator.get_page(page_number)
           return documents_paginated
        return render(self.request, self.template_name, {})
