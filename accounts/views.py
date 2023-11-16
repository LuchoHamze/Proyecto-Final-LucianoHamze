from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import MiFormularioDeCreacion, EdicionPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import DatosExtra

def login (request):
    
    formulario_de_login = AuthenticationForm()
    
    if request.method == 'POST':
        formulario_de_login = AuthenticationForm(request, data=request.POST)
        if formulario_de_login.is_valid():
            usuario = formulario_de_login.cleaned_data.get ("username")
            contra = formulario_de_login.cleaned_data.get ("password")
            
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect("inicio")  
        
    return render (request, "accounts/login.html", {"formulario_de_login": formulario_de_login})

def registro (request):
    formulario_de_registro = MiFormularioDeCreacion()
    
    if request.method == "POST":
        formulario_de_registro = MiFormularioDeCreacion(request.POST)
        if formulario_de_registro.is_valid():
            
            formulario_de_registro.save()
            
            return redirect("login")
    
    
    return render(request, "accounts/registro.html", {"formulario_de_registro": formulario_de_registro})

def editar_perfil (request):
    
    datos_extra = request.user.datosextra
    
    formulario_de_perfil = EdicionPerfil(initial={"biografia": datos_extra.biografia, "avatar": datos_extra.avatar}, instance=request.user)
    
    if request.method == "POST":
        formulario_de_perfil = EdicionPerfil(request.POST, request.FILES, instance= request.user)
        
        if formulario_de_perfil.is_valid():
            
            nueva_biografia = formulario_de_perfil.cleaned_data.get("biografia")
            nuevo_avatar = formulario_de_perfil.cleaned_data.get("avatar")
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                
                
            datos_extra.save()

            
            formulario_de_perfil.save()
            
            return redirect("editar_perfil")
    
    return render(request, "accounts/editar_perfil.html", {"formulario_de_perfil": formulario_de_perfil})

class CambiarPassword(PasswordChangeView):
    template_name = "accounts/cambiar_contrasenia.html"
    success_url = reverse_lazy ("editar_perfil")
    
    

