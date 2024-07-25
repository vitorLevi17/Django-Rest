from .serializers import *
from rest_framework import viewsets, generics

class EstudantesViewSet(viewsets.ModelViewSet):

    queryset = Estudantes.objects.all()
    serializer_class = EstudantesSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
class ListaMatriculaEstudante(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(id_estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(id_curs_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
