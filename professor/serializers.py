from rest_framework import serializers
from professor.models import Professor
from sala.serializers import AlunoSerializer


class ProfessorSerializer(serializers.Serializer):
    aluno = AlunoSerializer(many=True, read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.CharField()

    def create(self, validated_data):
        professor = Professor.objects.create(**validated_data)
        return professor

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.email = validated_data.get('email')
        instance.save()
        return instance