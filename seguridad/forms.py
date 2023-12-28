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
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('username', 'image')
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),max_length=15)
        self.fields['image'].widget = forms.FileInput(attrs={'class': 'form-control','id': 'image'})


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username','image')
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),max_length=15)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control','id': 'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control','id': 'password2'})
        self.fields['image'].widget = forms.FileInput(attrs={'class': 'form-control','id': 'image'})
           