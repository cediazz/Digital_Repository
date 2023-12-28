from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from seguridad.Utils import admin_restriction
from django.utils.decorators import method_decorator
from .settings import MEDIA_URL


@method_decorator(admin_restriction, name='dispatch')
class Home(View):
   template_name = 'Home.html'

   def get(self, request):
        return render(request, self.template_name,{'MEDIA_URL': MEDIA_URL})


