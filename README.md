# CRUD en Django para la Gestión de Productos en un Supermercado

Este proyecto es un prototipo de una funcionalidad CRUD desarrollada en Django. Permite listar productos disponibles en un supermercado y agregar nuevos registros a la base de datos.

## Características
- Listado de productos con id, nombre, descripción y precio.
- Formulario para agregar nuevos productos.
- Navegación sencilla entre la lista de productos y la página de creación de productos.

---

## Instalación y Configuración

### Requisitos previos
- Python 3.7 o superior
- Django 4.x

### Pasos de Instalación
1. Clona este repositorio.
   ```bash
   git clone <url_del_repositorio>
   cd supermercado
   ```
2. Instala Django si no lo tienes:
   ```bash
   pip install django
   ```
3. Aplica las migraciones para configurar la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
5. Visita la aplicación en tu navegador en `http://127.0.0.1:8000/`.

---

## Estructura del Proyecto
```
.
|-- supermercado/  # Proyecto principal
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- productos/     # Aplicación
|   |-- migrations/
|   |-- templates/
|   |   |-- productos/
|   |       |-- lista_productos.html
|   |       |-- agregar_producto.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- manage.py      # Archivo para ejecutar comandos
```

---

## Modelos

### Producto
El modelo de `Producto` define los campos básicos:
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
```

---

## Vistas

### Lista de Productos
La vista `lista_productos` muestra todos los productos almacenados en la base de datos:
```python
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})
```

### Agregar Producto
La vista `agregar_producto` permite crear nuevos registros mediante un formulario:
```python
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('lista_productos')
    return render(request, 'productos/agregar_producto.html')
```

---

## URLs

Configura las rutas en el archivo `urls.py`:

### URLs de la Aplicación `productos`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
]
```

### URLs Principales del Proyecto
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
]
```

---

## Plantillas HTML

### `lista_productos.html`
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Productos</title>
</head>
<body>
    <h1>Productos</h1>
    <table border="1">
        <tr>
            <th>id</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Precio</th>
        </tr>
        {% for producto in productos %}
        <tr>
            <td>{{ producto.id }}</td>
            <td>{{ producto.nombre }}</td>
            <td>{{ producto.descripcion }}</td>
            <td>{{ producto.precio }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{% url 'agregar_producto' %}">Agregar Producto</a>
</body>
</html>
```

### `agregar_producto.html`
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar Producto</title>
</head>
<body>
    <h1>Agregar Producto</h1>
    <form method="POST">
        {% csrf_token %}
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" id="nombre" required><br>
        <label for="descripcion">Descripción:</label>
        <textarea name="descripcion" id="descripcion" required></textarea><br>
        <label for="precio">Precio:</label>
        <input type="number" name="precio" id="precio" step="0.01" required><br>
        <button type="submit">Agregar</button>
    </form>
</body>
</html>
```

---

## Contribuciones
Si deseas contribuir a este proyecto, realiza un fork del repositorio, crea una rama nueva, realiza tus cambios y envía un pull request.

---

## Autor
Desarrollado por Daniela Miranda - Bootcamp Full Stack Python 2024-25.
