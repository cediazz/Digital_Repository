from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import MyUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=("nombre de usuario"),widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'name':'username', 'placeholder':'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword','name':'password', 'placeholder':'Password'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Password actual"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'id': 'floatingPassword',"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
        label=("Nuevo Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword',"autocomplete": "new-password"}),
        )
    new_password2 = forms.CharField(
        label=("Nuevo Password Confirmación"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword',"autocomplete": "new-password"}),
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'image']

    