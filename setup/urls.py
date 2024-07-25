from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import *

router = DefaultRouter(trailing_slash=False)
router.register(prefix='estudantes',viewset=EstudantesViewSet,basename='Estudantes')
router.register(prefix='cursos',viewset=CursoViewSet,basename='Cursos')
router.register(prefix='matriculas',viewset=MatriculaViewSet,basename='Matriculas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
]
