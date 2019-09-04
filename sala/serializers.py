from rest_framework import serializers 
from sala.models import Aluno
from sala.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('nome', 'idade')

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('nome', 'idade',)