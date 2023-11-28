from django.shortcuts import render
from django.views.generic import View

class Authenticate(View):
    def get(self,request):
        return render(request,'Sign-in/sign-in.html',{})
    