from .serializers import *
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from .throttle import MatriculaAnonRateThrottle

class EstudantesViewSet(viewsets.ModelViewSet):

    queryset = Estudantes.objects.all().order_by("id")
    serializer_class = EstudantesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['Nome']
    search_fields = ['Nome','CPF']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudantesSerializerV2
        return EstudantesSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]
class ListaMatriculaEstudante(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(id_estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudantesSerializer
class ListaMatriculaCurso(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(id_curs_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
