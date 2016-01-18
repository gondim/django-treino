
from django.conf.urls import url, include
from rest_framework import routers
from core import views
from django.conf.urls import url
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'Disciplina', views.DisciplinaViewSet)
router.register(r'Professor', views.ProfessorViewSet)
router.register(r'Curso', views.CursoViewSet)
router.register(r'Aluno', views.AlunoViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
