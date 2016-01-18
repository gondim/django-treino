from __future__ import unicode_literals

from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    professor = models.ForeignKey('Professor',on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso',on_delete=models.CASCADE)
    alunos = models.ManyToManyField('Aluno')

    def __str__(self):
    	return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
    	return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
    	return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey('Curso',on_delete=models.CASCADE)
    
    def __str__(self):
    	return self.nome