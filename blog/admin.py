from django.contrib import admin
from .models import Author, Post, Category

class PostInline(admin.TabularInline):
    model = Post
    extra = 1 #Nùmero de formularios vacìos para añadir posts

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'author', 'fecha_publicacion')
    list_filter = ('author', 'fecha_publicacion', 'categories')
    search_fields = ('titulo', 'contenido')
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register your models here.
