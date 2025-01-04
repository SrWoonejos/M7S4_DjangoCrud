from django.shortcuts import render, redirect
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('lista_productos')
    return render(request, 'productos/agregar_producto.html')
