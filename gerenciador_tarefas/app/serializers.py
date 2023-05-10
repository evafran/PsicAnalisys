
from rest_framework import serializers
from .models import Music
# from .models import Aluno
from .models import Tarefa

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:

        # model = Aluno
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tarefa
        fields = '__all__'