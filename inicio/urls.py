from django.urls import path
from inicio.views import inicio, paletas, explicacion_productos, tiendaproductos, productos_por_categorias, crear_producto, buscar_productos, eliminar_producto

urlpatterns = [
    path("", inicio, name="inicio"),
    path("paletas/", paletas, name= "paletas"),
    path("productos/", explicacion_productos, name= "productos"),
    path("tienda/", tiendaproductos, name= "tienda"),
    path('productos_por_categoria/<int:categoria_id>/', productos_por_categorias, name='productos_por_categoria'),
    path("crear_producto/", crear_producto, name= "crear_producto"),
    path('buscar_productos/', buscar_productos, name='buscar_productos'),
    path("tienda/<int:producto_id>/eliminar/", eliminar_producto, name= "eliminar_paleta")
]