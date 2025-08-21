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

## Plantillas 
- **Base:** 'blog/template/blog/base.html' define el diseño general con bloques 'title' y 'content'.
- **Lista de posts:** 'post_list.html' hereda de 'base.html', muestra posts con paginaciòn.
- **Detalles de post:** 'post_detail.html' hereda de 'base.html', muestra un post individual.
- **Contexto:** Usado para renderizar datos dinàmicos como '{{ post.titulo }}' y '{{ title }}'.

## Formularios
- **Formularios manual:** 'post_form.html' en '/posts/new/' permite crear posts con tìtulo, contenido, autor, y categorìas.
- **Vista:** 'post_create' (FBV) maneja 'GET' (mostrar formulario) y 'POST' (validar y guardar datos).
- **Validaciòn:** Manual, verificando tìtulo, contenido, autor, y categorìas con 'request.POST'.

## Formularios con ModelForm
- **Formulario:** PostForm en 'blog/forms.py' genera un formulario para crear posts basado en el modelo Post.
- **Vistas:** 
 - post_create (FBV): Usa PostForm para manejar GET/POST en /posts/new/.
 - PostCreateView (CBV): Usa CreateView con PostForm en /posts/new/manual/.
 - Comparando con post_create_manual (formulario manual en /posts/new/manual).
- **Ventajas:** Validaciòn automàtica, menos còdigo, e integraciòn con el ORM.
- **Plantillas:** post_form.html ModelForm, post_form_manual.html para el formulario manual.

## Sistema de usuarios
- **Autenticaciòn:** Usa django.contrib.auth con vistas integradas (LoginView, LogiutView) en /accounts/login/ y /accounts/logout/.
- **Registro:** Vista personalizada register en /accounts/register/ crea usuarios y asocia un Author.
- **Restricciones:** @login_required y LoginRequiredMixin protegen las vistas post_create y PostCreateView.
- **Plantillas:** login.html, logged_out.html, y register.html para autenticaciòn y registro.
- **Integraciòn:** Los posts se vinculan al Author del usuario autenticado (request.user).

## Mensajes y Feedback en la UI
- **Framework de mensajes:** Usa 'django.contrib.messages' para mostrar notificaciones de èxito (messages.succes) y (messages.error) en formularios de craciòn de posts, login, y registro.
- **Plantilla base:** 'base.html' muestra mensajes con estilos CSS para 'success', 'error', 'warnig', e 'info'.
- **Patròn Post/Redirect/Get:** Implementado en todas las vistas (post_create, PostCreateView, register, CustomLoginView) para evitar envìos duplicados.
- **Ejemplo:** Crear un por muestra "¡Post creado exitosamente!" en '/posts/'.

## CRUB (Create, Read, Update)
- **Create:** 'PostCreateView' y 'post_create' usan 'PostForm' para crear posts, restringidos a usuarios autenticados.
- **Read:** 'PostListView' lista posts con paginaciòn, y 'PostDetailView' muestra detalles.
- **Update:** 'PostUpdateView' permite editar post con 'UpdateView', restringiendo la ediciòn al autor del post.
- **Delete:** 'PostDeleteView' usa 'DeleteView' para eliminar posts, con confirmaciòn en 'post_confirm_delete.html' y restricciones al autor.
- **Platilla:** 'post_form.html' se reutilza para crear y editar, con mensajes de feedback.

## Permisos y Acceso
- **Permisos integrados:** Usa 'is_authenticated' para restringir vistas con 'LoginRequiredMixin' y '@login_required', redirigiendo a '/accounts/login/'.
- **Superusuarios:** 'is_superuser' permite a superusuarios editar/eliminar cualquier post en 'PostUpdateView' y 'PostDeleteView'.
- **Restriciòn al autor:** 'get_object' verifica que 'post.author.user == request.user' o 'request.user.is_superuser', lanzando Http404 si no cumple.
- **Plantillas:** 'post_detail.html' muestra enlaces de ediciòn/eliminaciòn solo para autores o superusuarios, con un mensaje para superusuarios. 