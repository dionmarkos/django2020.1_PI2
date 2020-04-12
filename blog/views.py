from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def lista_post(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'lista_post.html', {'posts':posts})

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detalhes.html', {'post': post})

def post_novo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detalhes', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_editar.html', {'form': form})

def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detalhes', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_editar.html', {'form': form})
