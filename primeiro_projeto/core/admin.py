from django.contrib import admin

from .models import Disciplina

from .models import Professor

from .models import Curso

from .models import Aluno

admin.site.register(Disciplina)

admin.site.register(Professor)

admin.site.register(Curso)

admin.site.register(Aluno)