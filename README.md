### Heroku
- URL: https://admin1-equipo7.herokuapp.com/
- admin: https://admin1-equipo7.herokuapp.com/admin
- Usuario administrador: username `admin` password `admin`


### Server local
- `python manage.py runserver` (corre en el puerto 8000)


### Admin local
- Para crear un usuario administrador: `python manage.py createsuperuser`
- URL: `localhost:8000/admin`


### Migraciones

- Generar migraciones: `python manage.py makemigrations`
- Correr migraciones: `python manage.py migrate`


### Librerías

- Instalar librerías del proyecto: `pip install -r requirements.txt`
- Al instalar una nueva librería: `pip freeze > requirements.txt`