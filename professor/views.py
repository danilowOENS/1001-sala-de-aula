from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from professor.models import Professor
from professor.serializers import ProfessorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProfessorViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer






# Create your views here.
