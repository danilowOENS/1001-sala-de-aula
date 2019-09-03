from django.shortcuts import render
from sala.models import Aluno


# Create your views here.

# def cadastrar(request):

#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('idade')
#         aluno.email = request.POST.get('email')
#         aluno.save()