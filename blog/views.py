from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post, Author, Category
from django.urls import reverse_lazy

def post_list(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']
    paginate_by = 2 # Muestra 2 posts por pàgina

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Posts Recientes'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

@login_required()
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get(user=request.user)
            post.save()
            form.save_m2m()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
def post_create_manual(request):
    if request.method == 'POST':
        errors = {}
        form_data = {
            'titulo': request.POST.get('titulo', ''),
            'contenido': request.POST.get('contenido', ''),
            'author': request.POST.get('author', ''),
            'categories': request.POST.getlist('categories', []),
        }

        if not form_data['titulo']:
            errors.setdefault('titulo', []).append('El tìtulo es obligatorio.')
        elif len(form_data['titulo']) > 200:
            errors.setdefault('titulo', []).append('El tìtulo no puede exceder 200 caracteres.')

        if not form_data['contenido']:
            errors.setdefault('contenido', []).append('El contenido es obligatorio.')

        if not form_data['author']:
            errors.setdefault('author', []).append('Debe seleccionar un autor.')
        else:
            try:
                Author.objects.get(id=form_data['author'])
            except Author.DoesNotExist:
                errors.setdefault('author', []).append('El autor seleccionado no existe.')

        if not form_data['categories']:
            errors.setdefault('categories', []).append('Debe seleccionar al menos una categoria.')
        else:
            for cat_id in form_data['categories']:
                try:
                    Category.objects.get(id=cat_id)
                except Category.DoesNotExist:
                    errors.setdefault('categories', []).append(f'La categoria con ID {cat_id} no existe.')

        if not  errors:
            post = Post.objects.create(
                titulo=form_data['titulo'],
                contenido=form_data['contenido'],
                author_id=form_data['author'],
            )
            post.categories.set(form_data['categories'])
            return redirect('blog:post_list')

        return render(request, 'blog/post_form_manual.html', {
            'errors': errors,
            'form_data': form_data,
            'author': Author.objects.all(),
            'categories': Category.objects.all(),
        })

    return render(request, 'blog/post_form_manual.html', {
        'author': Author.objects.all(),
        'categories': Category.objects.all(),
    })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(
                user=user,
                name=user.username,
                email=user.email or f"{user.username}@example.com",
            )
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})