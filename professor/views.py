from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from professor.models import Professor
from professor.serializers import ProfessorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = (ProfessorSerializer,)






# Create your views here.
