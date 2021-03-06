from models import Disciplina,Professor,Curso,Aluno
from rest_framework import serializers


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = ('nome', 'professor', 'curso','alunos')

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('nome')

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('nome')


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ('nome','curso')
