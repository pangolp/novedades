## Modulo de Python / Django para la administración de novedades.

### Instalación:

Clonar el repositorio, recomendamos tener un directorio de aplicaciones.
* Por ejemplo, "modules" o "apps"

```sh
$ git clone https://github.com/pangolp/novedades.git
```

### Requerimientos

```
django-ckeditor==5.7.1
django-crispy-forms==1.7.2
django-js-asset==1.2.2
```

### Agregamos el modulo en el settings.py

```python
INSTALLED_APPS = [
	...
	'novedades',
	'ckeditor',
	...
]
```

### Recomendamos dividir INSTALLED_APPS en 3:
* DJANGO_APPS para las aplicaciones propias del framework
* THIRD_PARTY_APPS para las aplicaciones de terceros (como este repositorio)
* LOCAL_APPS para las aplicaciones propias de su proyecto

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

### Aplicar las migraciones
```sh
$ python manage.py migrate
```
