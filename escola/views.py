from .serializers import *
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from .throttle import MatriculaAnonRateThrottle

class EstudantesViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """

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
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """

    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]

    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    """
        Descrição da View:
        - Lista Matriculas por id de Estudante
        Parâmetros:
        - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
        """
    def get_queryset(self):
        queryset = Matricula.objects.filter(id_estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
       Descrição da View:
       - Lista Matriculas por id de Curso
       Parâmetros:
       - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
       """

    def get_queryset(self):
        queryset = Matricula.objects.filter(id_curs_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
