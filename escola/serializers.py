from rest_framework import serializers
from .models import Curso,Estudantes

class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = ['id','Nome','Email','CPF','Data_Nascimento','Celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'