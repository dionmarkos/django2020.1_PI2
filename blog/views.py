from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm
from django.contrib.auth.decorators import login_required

def post_lista(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'post_lista.html', {'posts':posts})

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detalhes.html', {'post': post})

@login_required
def post_novo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detalhes', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_editar.html', {'form': form})

@login_required
def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detalhes', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_editar.html', {'form': form})

@login_required
def post_lista_rascunhos(request):
    posts = Post.objects.filter(data_publicacao__isnull=True).order_by('data_criacao')
    return render(request, 'post_lista_rascunhos.html', {'posts': posts})

@login_required
def post_publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publicar()
    return redirect('post_detalhes', pk=pk)

@login_required
def post_remover(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_lista')

def add_comentario_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('post_detalhes', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'add_comentario_post.html', {'form': form})

@login_required
def comentario_aprovar(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.aprovar()
    return redirect('post_detalhes', pk=comentario.post.pk)

@login_required
def comentario_remover(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    return redirect('post_detalhes', pk=comentario.post.pk)
