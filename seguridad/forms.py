from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'name':'username', 'placeholder':'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword','name':'password', 'placeholder':'Password'}))