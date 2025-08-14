from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categories']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 5}),
            'categories': forms.SelectMultiple(attrs={'size': 5}),
        }
        labels = {
            'titulo' : 'Tìtulo',
            'contenido' : 'Contenido',
            'categories' : 'Categorìas',
        }