from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'), # FBV
    path('cbv/', views.PostListView.as_view(), name='post_list_cbv'), # CBV
]