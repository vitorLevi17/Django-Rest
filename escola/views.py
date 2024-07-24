from .models import *
from .serializers import *
from rest_framework import viewsets

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudantes.objects.all()
    serializer_class = EstudantesSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
