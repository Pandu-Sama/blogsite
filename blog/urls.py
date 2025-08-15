from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'), # FBV
    path('cbv/', views.PostListView.as_view(), name='post_list_cbv'), # CBV
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('new/cbv/', views.PostCreateView.as_view(), name='post_create_cbv'),
    path('new/manual/', views.post_create_manual, name='post_create_manual'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
]