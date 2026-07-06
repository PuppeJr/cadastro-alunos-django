# alunos/admin.py
from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento', 'data_cadastro')
    search_fields = ('nome', 'email')