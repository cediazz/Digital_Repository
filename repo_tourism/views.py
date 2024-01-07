from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from seguridad.Utils import admin_restriction
from django.utils.decorators import method_decorator
from .settings import MEDIA_URL
from repository.models import Document
from django.core.paginator import Paginator

@method_decorator(admin_restriction, name='dispatch')
class Home(View):
   template_name = 'Home.html'
   items_per_page = 6

   def get(self, request):
        documents = None
        if 'title' in request.GET:
          documents = Document.objects.filter(title__icontains = request.GET['title']).order_by('-publication_date')
        else:
         documents = Document.objects.order_by('-publication_date')
        # Paginar los resultados
        paginator = Paginator(documents, self.items_per_page)
        page_number = request.GET.get('page')
        documents_paginated = paginator.get_page(page_number)
        return render(request, self.template_name,{'documents_paginated':documents_paginated})


