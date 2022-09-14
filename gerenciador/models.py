from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=65)
    slug = models.SlugField()
    descricao = models.CharField(max_length=65)
    explicacao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    esta_publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    imagem = models.ImageField(
        upload_to='projetos/imagens/%Y/%m/%d', blank=True, default=''
    )

    def __str__(self) -> str:
        return self.titulo