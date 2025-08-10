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
- **Category:** Nombre de la categorìa.
- **Post:** Almacena el tìtulo, contenido, fecha, autor (ForeignKey), categorìas (ManyToManyField).
- **Consultas ORM:** Ejemplos incluyen filtrar posts por author ('Post.objects.filter(author__name="David")'), por fecha ('fecha_publicacion__year=2025'), y combinar condiciones con 'Q'.

## Admin
- **Modelos regitrados:** 'Author', 'Post', 'Category'.
- **Personalizaciones:** Listado con 'list_display', filtrado con 'list_filter', bùsqueda con 'search_fields', navegaciòn por fechas en 'Post'. Inline para gestionar posts desde 'Author'
- **Acceso:** '/admin/' con un superusuario.

## Vistas
- **FBV:** 'post_list' en 'blog/views.py' lista posts en '/posts/'.
- **CBV:** 'PostListView' (hereda de 'ListView') lista posts en '/posts/cbv/' con pafinaciòn y tìtulo dinàmico.
- **Plantillas:** 'blog/templates/post_list.html' muestra la lista de posts.

## Rutas 
- **URLs:** Definidas en 'blog/urls.py' con 'app_name = 'blog''.
- **Rutas configuradas:**
  - '/posts/': Lista de posts ('blog:post_list', usa 'PostListView').
  - '/posts/<pk>': Detalles de un post ('blog:post_datail', usa 'PostDetailView').
- **Platillas:** 'post_list.html' y 'post_detail.html' en 'blog/template/blog/'.
