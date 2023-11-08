from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

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

