# Blogsite 
Un proyecto base Django para un blog

## Instalaciòn
1. Clona el repositorio: https://github.com/Pandu-Sama/blogsite.git
2. Crea un entorno virtual: 'python -m venv djangoenv'
3. Activa el entorno: 'source django/bin/activate'
4. Instala Django: 'pip install django=5.2.4'
5. Aplica migraciones: 'python manage.py migrate'
6. Inicia el servidor: 'python manage.py runserver'

## Modelos
- **Author:** Almacena el nombre y correo del autor (ùnico).
- **Post:** Almacena el tìtulo, contenido, fecha de publicaciòn, y una relaciòn ForeignKey con Author.
