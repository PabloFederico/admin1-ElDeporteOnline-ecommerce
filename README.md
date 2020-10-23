### Admin
- Para crear un usuario administrador: `python manage.py createsuperuser`
- URL: `localhost:8000/admin`


### Server local
- `python manage.py runserver` (corre en el puerto 8000)


### Migraciones

- Generar migraciones: `python manage.py makemigrations`
- Correr migraciones: `python manage.py migrate`


### Librerías

- Instalar librerías del proyecto: `pip install -r requirements.txt`
- Al instalar una nueva librería: `pip freeze > requirements.txt`