# Instrucciones para Configurar y Ejecutar el Proyecto To Do App Django

## Prerrequisitos

Asegúrate de tener instalados los siguientes software en tu máquina:

* Python 3.x (recomendado Python 3.8 o superior)
* pip (gestor de paquetes de Python)
* git (para clonar el repositorio)
* MacOS/Linux o descargar terminal en VSC Ubuntu (WSL).Mas informacion [Aqui](https://learn.microsoft.com/es-es/windows/wsl/tutorials/wsl-vscode).

## Pasos para Configurar el Entornor

### 1. Clonar el Repositorio
Primero, clona el repositorio de tu proyecto desde GitHub (o cualquier otro sistema de control de versiones que estés usando ):

```
git clone https://github.com/Jaimeangel/To-Do-App-Django-ProTalento.git
cd Do-App-Django-ProTalento
```

### 2. Crear un Entorno Virtual
Crea un entorno virtual para aislar las dependencias del proyecto. Esto evita conflictos entre paquetes de diferentes proyectos:

```
pip install virtualenv
```

```
python -m venv env
```

### 3. Activar el Entorno Virtual
```
source env/bin/activate
```

### 4. Instalar las Dependencias
Una vez activado el entorno virtual, instala las dependencias del proyecto desde el archivo requirements.txt:
```
pip install -r requirements.txt
```

### 5. Configurar la Base de Datos
Realiza las migraciones necesarias para configurar la base de datos:
```
python manage.py migrate
```
### 6. Crear un Superusuario
Crea un superusuario para acceder al administrador de Django:
```
python manage.py createsuperuser
```
Sigue las instrucciones que aparecen en pantalla para completar la creación del superusuario.

### 7. Ejecutar el Servidor de Desarrollo
Finalmente, ejecuta el servidor de desarrollo de Django:
```
python manage.py runserver
```
Abre tu navegador web y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

### 8. Acceder a la aplicacion como usuario regular o como super usuario
Abre tu navegador web y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento. 
* Para ingresar como superadmin sigues las siguientes instrucciones:
Accede a la interfaz de administración en http://127.0.0.1:8000/admin/ usando las credenciales del superusuario que creaste anteriormente.
* Para acceder como usuario regular, puedes crear una cuenta dando click en la pagina de /login en : Crear cuenta, al final del formulario. Ingresa tus datos solicitados en el formulario y despues da click en crear cuenta. Seras redirigido a la pagina principal
* Si ya cuentas con una cuenta creada, ya puedes ingresar a la aplicacion por medio de la pagina login con tus credenciales previamente creadas.


## Notas Adicionales
* Desactivar el Entorno Virtual: Para desactivar el entorno virtual, simplemente ejecuta:
```
deactivate
```
* Actualizar Dependencias: Si agregas nuevas dependencias al proyecto, asegúrate de actualizar el archivo requirements.txt:
```
pip freeze > requirements.txt
```
* Archivos Ignorados: Asegúrate de que los archivos sensibles y las carpetas como el entorno virtual y la base de datos estén listados en el archivo .gitignore para no subirlos al repositorio. Un ejemplo de .gitignore podría ser:
```
# .gitignore
env/
*.pyc
__pycache__/
db.sqlite3
```

## Conclusión
Con estos pasos, deberías poder configurar y ejecutar tu proyecto Django sin problemas. Si tienes alguna pregunta o encuentras algún problema, no dudes en escribirme a mi correo: jaimeangel1097@gmail.com

Sigueme en mis redes sociales
* [LinkedIn](https://www.linkedin.com/in/jaimeangeldev/).
* [GitHub](https://github.com/Jaimeangel/)


# Descripción de la estructura del proyecto y las decisiones de diseño importantes.

### Estructura de Archivos y Carpetas

El proyecto Django sigue una estructura de carpetas estándar, pero con algunas modificaciones para integrar Bootstrap 5 y organizar los archivos de manera efectiva.

- **Directorio del Proyecto**: Este es el directorio principal del proyecto Django.
    - **`manage.py`**: Script para administrar el proyecto Django.
    - **Directorio de la Aplicación Principal**: Este directorio contiene la configuración principal del proyecto Django.
        - **`settings.py`**: Archivo de configuración principal donde se definen todas las configuraciones del proyecto.
        - **`urls.py`**: Archivo de configuración de las URL del proyecto.
        - **`wsgi.py`**: Archivo de entrada para el servidor WSGI (Web Server Gateway Interface).
        - **`asgi.py`**: Archivo de entrada para el servidor ASGI (Asynchronous Server Gateway Interface) para aplicaciones asincrónicas.
    - **Directorio de Aplicaciones**: Este directorio contiene las aplicaciones Django individuales.
    - **Directorio de Plantillas (Templates)**: Aquí se almacenan los archivos HTML de las plantillas de la aplicación.
    - **Directorio de Archivos Estáticos**: Este directorio almacena archivos estáticos como CSS, JavaScript, imágenes, etc.
        - **`static/`**: Carpeta principal para archivos estáticos.
            - **`css/`**: Carpeta para archivos CSS personalizados.
            - **`js/`**: Carpeta para archivos JavaScript personalizados.
            - **`img/`**: Carpeta para imágenes y otros recursos visuales.

### Decisiones de Diseño Importantes

1. **Uso de Bootstrap 5**: Se eligió Bootstrap 5 como el framework de diseño para proporcionar una interfaz de usuario moderna, receptiva y fácil de usar. Bootstrap 5 ofrece una amplia gama de componentes y estilos predefinidos que aceleran el proceso de desarrollo y garantizan una apariencia consistente en todo el sitio web.

2. **Integración con Django**: Se aprovechó la capacidad de Django para gestionar plantillas y archivos estáticos de manera eficiente. Se utilizó la configuración adecuada en `settings.py` para establecer las rutas de los archivos estáticos y de las plantillas, asegurando así una integración fluida con Bootstrap 5.

3. **Organización de Archivos Estáticos**: Se organizó cuidadosamente la estructura de archivos estáticos para mantener un código limpio y modular. Los archivos CSS personalizados se ubicaron en su propia carpeta dentro del directorio estático para facilitar su mantenimiento y extensión.

4. **Plantillas Reutilizables**: Se crearon plantillas HTML reutilizables para componentes comunes como encabezados, pies de página, barras de navegación, etc. Esto ayuda a mantener la consistencia en todo el sitio web y a facilitar la modificación y actualización futuras.