from .models import Estudantes,Curso
from .serializers import EstudantesSerializer,CursoSerializer
from rest_framework import viewsets

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudantes.objects.all()
    serializer_class = EstudantesSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
