from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from inicio.models import Paleta, Producto, Categoria, Subcategoria
from .forms import BusquedaForm, ProductoForm

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
    
def crear_producto(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("productos")
            # Aquí puedes redirigir a la página de éxito o hacer lo que necesites
    else:
        form = ProductoForm()

    return render(request, "inicio/crear_producto.html", {'categorias': categorias, 'subcategorias': subcategorias, 'form': form})    

def lista_productos(request):
    productos = Producto.objects.all()
    form = BusquedaForm(request.GET)  # Recupera los datos del formulario GET

    if form.is_valid():
        busqueda = form.cleaned_data['busqueda']
        productos = productos.filter(nombre__icontains=busqueda)

    return render(request, 'inicio/tienda.html', {'productos': productos, 'form': form})

def buscar_productos(request):
    
    if request.GET:
        
        buscador = Producto.objects.filter(nombre__icontains = request.GET["buscar"])
        
        contexto = { "buscados" : buscador}
        
        plantilla = loader.get_template("inicio/tienda.html")
        
        documento = plantilla.render (contexto)
        return HttpResponseRedirect(documento)
    else:
        contexto = { "mensaje" : "No existe"}
        
    plantilla = loader.get_template("inicio/tienda.html")
    documento = plantilla.render (contexto)
    return HttpResponseRedirect(documento)    