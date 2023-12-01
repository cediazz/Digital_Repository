from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    dic = {'saludo':"Hola"}

    return render(request,'Home.html',dic)