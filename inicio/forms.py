from django import forms
from .models import Producto

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar')
    

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', "stock", 'categoria', 'subcategoria']   
        
class ActualizarProductoFormulario (forms.ModelForm):  
     class Meta:
        model = Producto
        fields = ['nombre', 'precio', "stock", 'categoria', 'subcategoria']       