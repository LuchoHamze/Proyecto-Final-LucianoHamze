from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from inicio.models import Paleta, Producto, Categoria, Subcategoria
from inicio.forms import ActualizarProductoFormulario
from .forms import BusquedaForm, ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

def inicio (request):
    return render (request, "inicio/inicio.html", {})

def paletas (request):
    
    paleta = Paleta (marca= "Wilson", descripcion = "Tenis", anio=2022)
    paleta.save () 
    return render (request, "inicio/paletas.html", {"paleta": paleta})

#def explicacion_productos (request):
 #   return render (request, "inicio/productos.html", {})
 
def explicacion_productos(request):
    categorias = Categoria.objects.all()
    return render(request, "inicio/tienda.html", {'categorias': categorias}) 

def productos_por_categorias (request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'productos': productos}
    return render(request, 'inicio/tienda.html', context)

def tiendaproductos (request):
    productos = Producto.objects.all()
    return render (request, "inicio/tienda.html", {'productos': productos})

# def crear_productos(request):
#     categorias = Categoria.objects.all()

#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         stock = request.POST.get('stock')
#         precio = request.POST.get('precio')
#         categoria_id = request.POST.get('categoria')
#         subcategoria_id = request.POST.get('subcategoria')

#         producto = Producto(nombre=nombre, precio=precio, stock = stock, categoria_id = categoria_id, subcategoria_id = subcategoria_id)
#         producto.save()

    # return render(request, "inicio/crear_producto.html", {'categorias': categorias})

@login_required    
def crear_producto(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("productos")
    else:
        form = ProductoForm()

    return render(request, "inicio/crear_producto.html", {'categorias': categorias, 'subcategorias': subcategorias, 'form': form})  

def eliminar_producto(request, producto_id):
    producto_a_eliminar = Producto.objects.get(id=producto_id)
    producto_a_eliminar.delete()
    return redirect("tienda")

def actualizar_producto(request, producto_id):
    producto_a_actualizar = Producto.objects.get(id=producto_id)
    
    if request.method == "POST":
        formulario_de_actualizar = ActualizarProductoFormulario(request.POST)
        if formulario_de_actualizar.is_valid():
            info_nueva = formulario_de_actualizar.cleaned_data
            
            producto_a_actualizar.nombre = info_nueva.get("nombre")
            producto_a_actualizar.precio = info_nueva.get("precio")
            producto_a_actualizar.stock = info_nueva.get("stock")
            producto_a_actualizar.categoria = info_nueva.get("categoria")
            producto_a_actualizar.subcategoria = info_nueva.get("subcategoria")
            
            producto_a_actualizar.save()
            return redirect ("tienda")
        return render (request, "inicio/actualizar_producto.html", {"formulario_de_actualizar" : formulario_de_actualizar})    
    
    formulario_de_actualizar = ActualizarProductoFormulario (initial = {"nombre": producto_a_actualizar.nombre, "precio": producto_a_actualizar.precio, "stock" : producto_a_actualizar.stock, "categoria": producto_a_actualizar.categoria, "subcategoria":producto_a_actualizar.subcategoria})
    return render (request, "inicio/actualizar_producto.html", {"formulario_de_actualizar" : formulario_de_actualizar})

def lista_productos(request):
    productos = Producto.objects.all()
    form = BusquedaForm(request.GET) 

    if form.is_valid():
        busqueda = form.cleaned_data['busqueda']
        productos = productos.filter(nombre__icontains=busqueda)       

    return render(request, 'inicio/tienda.html', {'productos': productos, 'form': form})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    return render(request, "inicio/detalle_producto.html", {"producto": producto})

def buscar_productos(request):
    
    if request.GET:
        
        buscador = Producto.objects.filter(nombre__icontains = request.GET["buscar"])
        
        contexto = { "buscados" : buscador}
        
        return render(request, "inicio/tienda.html", contexto)
    else:
        contexto = { "mensaje" : "No existe"}
    
    return render(request, "inicio/tienda.html")

def acerca_de_mi(request):
    
    return render(request, "inicio/acerca_de_mi.html")
