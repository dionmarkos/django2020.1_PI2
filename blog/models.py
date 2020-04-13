from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def comentarios_aprovados(self):
        return self.comentarios.filter(comentario_aprovado=True)

class Comentario(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    comentario_aprovado = models.BooleanField(default=False)

    def aprovar(self):
        self.comentario_aprovado = True
        self.save()

    def __str__(self):
        return self.text
