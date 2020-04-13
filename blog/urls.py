from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
    path('post/<int:pk>/', views.post_detalhes, name='post_detalhes'),
    path('post/novo/', views.post_novo, name='post_novo'),
    path('post/<int:pk>/editar/', views.post_editar, name='post_editar'),
    path('rascunhos/', views.post_lista_rascunhos, name='post_lista_rascunhos'),
    path('post/<pk>/publicar/', views.post_publicar, name='post_publicar'),
    path('post/<pk>/remover/', views.post_remover, name='post_remover'),
    path('post/<int:pk>/comentar/', views.add_comentario_post, name='add_comentario_post'),
    path('comentario/<int:pk>/aprovar/', views.comentario_aprovar, name='comentario_aprovar'),
    path('comentario/<int:pk>/remover/', views.comentario_remover, name='comentario_remover'),
]
