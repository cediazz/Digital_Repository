from django.shortcuts import render
from Digital_Repository.settings import MEDIA_URL

# Decorador que no permite acceder a una vista si hay un administrador logeado
def admin_restriction(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            # Redirigir a una plantilla HTML de error
            return render(request,'MaintenanceTemplate.html',{'MEDIA_URL': MEDIA_URL})
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
 
 