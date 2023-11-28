from django.shortcuts import render

def saludo(request):
    dic = {'saludo':"Hola"}

    return render(request,'Prueba.html',dic)