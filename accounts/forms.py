from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField (label= "Contrasena", widget= forms.PasswordInput)
    password2 = forms.CharField (label= "Repetir Contrasena", widget= forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {key: " " for key in fields}
        
class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label= "Cambiar Correo electrónico", required=False)
    first_name = forms.CharField(label= "Nombre", required=False)
    last_name =  forms.CharField(label= "Apellido", required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]