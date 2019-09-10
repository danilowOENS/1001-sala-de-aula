from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from sala.models import Aluno
from sala.serializers import AlunoSerializer, AlunoLightSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Aluno.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer

class AlunoList(views.APIView):
    def get (self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoLightSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,resquest):
        serializer = AlunoSerializer(data=resquest.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AlunoDetails(views.APIView):

    def get_object(self, id):
        try:
            return Aluno.objects.get(id=id)
        except:
            raise Http404

    def get (self, request, id):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, id):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)





# Create your views here.
# def cadastrar(request):

#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('idade')
#         aluno.email = request.POST.get('email')
#         aluno.save()