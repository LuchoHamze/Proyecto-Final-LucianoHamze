from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

class MiFormularioDeCreacion(UserCreationForm):
    username = forms.CharField(label= "Nombre de Usuario")
    email = forms.EmailField()
    password1 = forms.CharField (label= "Contrasena", widget= forms.PasswordInput)
    password2 = forms.CharField (label= "Repetir Contrasena", widget= forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre")
    last_name =  forms.CharField(label= "Apellido")
    # biografia = forms.CharField(label= "Biografia", widget=forms.Textarea)
    # avatar = forms.ImageField(label= "Avatar")
    
    class Meta:
        
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_text = {key: " " for key in fields}
        
class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label= "Cambiar Correo electrónico", required=False)
    first_name = forms.CharField(label= "Nombre", required=False)
    last_name =  forms.CharField(label= "Apellido", required=False)
    biografia = RichTextFormField(label= "Biografia", required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "biografia", "avatar"]
        
class Perfil():
    ...