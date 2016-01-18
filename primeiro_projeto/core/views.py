from models import Disciplina,Professor,Curso,Aluno
from rest_framework import viewsets
from serializers import DisciplinaSerializer,ProfessorSerializer,CursoSerializer,AlunoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

