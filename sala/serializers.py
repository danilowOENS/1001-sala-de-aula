from rest_framework import serializers 
from sala.models import Aluno
from sala.models import Professor


class AlunoSerializer(serializers.Serializer):
    id = serializers.ImageField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.CharField()

    prof_favorito = serializers.SlugRelatedField(
        slug_field='nome',
        queryset=Professor.objects.all()
    )


    def create(self, validated_data):
        aluno =Aluno.objects.create(**validated_data)
        return aluno

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.email = validated_data.get('email')
        instance.prof_favorito = validated_data.get('prof_favorito')
        instance.save()
        return instance