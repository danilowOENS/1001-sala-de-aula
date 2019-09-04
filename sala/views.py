from django.shortcuts import render
from rest_framework import viewsets
from sala.models import Aluno
from sala.serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer




# Create your views here.
# def cadastrar(request):

#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('idade')
#         aluno.email = request.POST.get('email')
#         aluno.save()