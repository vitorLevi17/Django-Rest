from django.test import TestCase
from escola.models import Estudantes,Curso
from escola.serializers import EstudantesSerializer,CursoSerializer

class serializerEstuanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudantes(Nome="Teste de Modelo da Silva",
                                    Email="Testeeee@gmail.com",
                                    CPF=38225551001,
                                    Data_Nascimento='2000-02-02',
                                    Celular='86 99999-8888')
        self.serializer_estudante = EstudantesSerializer(instance=self.estudante)

    def test_verifica_Estudante_Serializer(self):
        """Teste verifica campos serializados do Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()),set(['id','Nome','Email','CPF','Data_Nascimento','Celular']))
    def test_verifica_Campos_Serializer_Estudante(self):
        """Teste verifica o conteudo dos campos serializados do Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['Nome'],self.estudante.Nome)
        self.assertEqual(self.estudante.Email, self.estudante.Email)
        self.assertEqual(self.estudante.CPF, self.estudante.CPF)
        self.assertEqual(self.estudante.Data_Nascimento, self.estudante.Data_Nascimento)
        self.assertEqual(self.estudante.Celular, self.estudante.Celular)

class serializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(id_curso='POO1',
                           Descricao='Curso de programação orientada a objetos 1',
                           Nivel='I')
        self.serializer_curso = CursoSerializer(instance=self.curso)
    def test_verifica_Curso_Serializer(self):
        """Teste verifica campos serializados do Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()),set(['id','id_curso','Descricao','Nivel']))
    def test_verifica_Campos_Serializer_Curso(self):
        """Teste verifica o conteudo dos campos serializados do Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(dados['id_curso'],self.curso.id_curso)
        self.assertEqual(self.curso.Descricao, self.curso.Descricao)
        self.assertEqual(self.curso.Nivel, self.curso.Nivel)
