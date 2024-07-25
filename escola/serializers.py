from rest_framework import serializers
from .models import *

class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = ['id','Nome','Email','CPF','Data_Nascimento','Celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='id_curs.Descricao') #GPT
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='id_estudante.Nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']