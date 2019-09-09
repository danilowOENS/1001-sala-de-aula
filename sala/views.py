from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from sala.models import Aluno
from sala.serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Aluno.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer





# Create your views here.
# def cadastrar(request):

#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('idade')
#         aluno.email = request.POST.get('email')
#         aluno.save()