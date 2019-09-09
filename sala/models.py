from django.db import models

# Create your models here.
from professor.models import Professor


class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome')

    idade = models.CharField(
        max_length=50,
        verbose_name='idade')

    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True)

    prof_favorito = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='alunos'
    )

    def __str__(self):
        return self.nome

