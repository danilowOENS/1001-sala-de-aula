from professor.models import Professor
from rest_framework import serializers


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('nome', 'idade')