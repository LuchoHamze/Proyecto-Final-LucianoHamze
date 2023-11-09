from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import MiFormularioDeCreacion

def login (request):
    
    formulario_de_login = AuthenticationForm()
    
    if request.method == 'POST':
        formulario_de_login = AuthenticationForm(request, data=request.POST)
        if formulario_de_login.is_valid():
            usuario = formulario_de_login.cleaned_data.get ("username")
            contra = formulario_de_login.cleaned_data.get ("password")
            
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
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

