from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

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

