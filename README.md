# Proyecto CRUD en Django - Sitio de Supermercado

## Descripción
Este proyecto es un prototipo de funcionalidad para el sitio web de un supermercado, desarrollado en Django y Python. La aplicación permite listar productos en una tabla y añadir registros de productos de forma dinámica.

## Características
- Listado de productos con columnas de ID, nombre, descripción y precio.
- Funcionalidad para agregar un nuevo producto a la tabla.
- Implementado usando un entorno virtual para gestionar dependencias.

## Requisitos previos
- Python 3.8 o superior.
- Django 4.0 o superior.
- Pip instalado.

## Configuración del entorno virtual
1. **Crear el entorno virtual:**
   ```bash
   python -m venv venv
   ```
2. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Instalar dependencias:**
   ```bash
   pip install django
   ```

## Instrucciones de instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto-supermercado.git
   ```
2. Navegar al directorio del proyecto:
   ```bash
   cd proyecto-supermercado
   ```
3. Configurar el entorno virtual siguiendo los pasos mencionados anteriormente.
4. Aplicar las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
5. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso
1. Accede a la vista principal en tu navegador:
   ```
   http://127.0.0.1:8000/
   ```
2. Visualiza los productos listados en la tabla.
3. Agrega un nuevo producto haciendo clic en el enlace "Agregar Producto" y completando el formulario correspondiente.

## Estructura del Proyecto
```
proyecto-supermercado/
├── manage.py
├── supermercado/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── productos/
│   ├── migrations/
│   ├── templates/
│   │   └── productos/
│   │       ├── lista.html
│   │       └── agregar.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
└── venv/
```

## Tecnologías utilizadas
- Django: Framework principal para el desarrollo.
- Python: Lenguaje de programación.
- HTML: Para el diseño de las vistas.
- Entorno virtual: Para gestionar las dependencias del proyecto.

## Contribuciones
Si deseas contribuir a este proyecto, por favor, sigue los pasos a continuación:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Agregada nueva funcionalidad"
   ```
4. Envía tus cambios mediante un pull request.

## Licencia
Este proyecto está bajo la licencia MIT. Para más información, consulta el archivo LICENSE.
