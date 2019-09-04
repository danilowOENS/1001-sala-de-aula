from django.db import models


# Create your models here.
class Professor(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='nome')

    idade = models.CharField(
        max_length=50,
        verbose_name='idade')