from rest_framework import serializers 
from sala.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('nome', 'idade', 'email')