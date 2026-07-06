# alunos/models.py

from django.db import models

class Aluno(models.Model):
    """
    Modelo que representa um aluno.
    """
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome completo'
    )
    data_nascimento = models.DateField(
        verbose_name='Data de nascimento'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='E-mail'
    )
    telefone = models.CharField(
        max_length=20,
        blank=True,  # opcional
        verbose_name='Telefone'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,  # preenche automaticamente na criação
        verbose_name='Data de cadastro'
    )

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']  # ordena por nome

    def __str__(self):
        return self.nome