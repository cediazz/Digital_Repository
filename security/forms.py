from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm,UserCreationForm
from .models import MyUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=("nombre de usuario"),widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}),max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))

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

class UserUpdateForm(UserChangeForm):
    class Meta():
        model = MyUser
        fields = ('username', 'image')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'image': forms.FileInput(attrs={'class': 'form-control','id': 'image'})
           }
   
        

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username','image')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'image': forms.FileInput(attrs={'class': 'form-control','id': 'image'}),
            }
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control','id': 'password1'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control','id': 'password2'}))
    
           