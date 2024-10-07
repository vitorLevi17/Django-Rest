from django.test import TestCase
from escola.models import Estudantes,Matricula,Curso

class modelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudantes.objects.create(Nome = "Teste de Modelo da Silva",
                                                   Email = "Testeeee@gmail.com",
                                                   CPF = 38225551001,
                                                   Data_Nascimento = '2000-02-02',
                                                   Celular = '86 99999-8888')
    # def testeFalha(self):
    #     self.fail('Teste falhou :(')
    def testVerificaAtributos(self):
        """
        Teste que verifica os atributos do modelo de estudante
        """
        self.assertEqual(self.estudante.Nome,'Teste de Modelo da Silva')
        self.assertEqual(self.estudante.Email, 'Testeeee@gmail.com')
        self.assertEqual(self.estudante.CPF, 38225551001)
        self.assertEqual(self.estudante.Data_Nascimento,'2000-02-02')
        self.assertEqual(self.estudante.Celular,'86 99999-8888')

class modelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(id_curso = 'POO1',
                                          Descricao = 'Curso de programação orientada a objetos 1',
                                          Nivel = 'I')

    # def testeFalha(self):
    #     self.fail('Teste falhou :(')

    def testVerificaAtributos(self):
        """
        Teste que verifica os atributos do modelo de Curso
        """
        self.assertEqual(self.curso.id_curso,'POO1')
        self.assertEqual(self.curso.Descricao, 'Curso de programação orientada a objetos 1')
        self.assertEqual(self.curso.Nivel,'I')

class modelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudantes.objects.create(Nome = "Teste de Modelo da Silva",
                                                             Email = "Testeeee@gmail.com",
                                                             CPF = 38225551001,
                                                             Data_Nascimento = '2000-02-02',
                                                             Celular = '86 99999-8888')

        self.curso_matricula = Curso.objects.create(id_curso = 'POO1',
                                                    Descricao = 'Curso de programação orientada a objetos 1',
                                                    Nivel = 'I')
        self.matricula = Matricula.objects.create(
            id_estudante=self.estudante_matricula,
            id_curs=self.curso_matricula,
            periodo='M'
        )

    def testVerificaAtributos(self):
        """
        Teste que verifica os atributos do modelo da Matricula
        """
        self.assertEqual(self.matricula.id_estudante.Nome,'Teste de Modelo da Silva')
        self.assertEqual(self.matricula.id_curs.id_curso, 'POO1')
        self.assertEqual(self.matricula.periodo,'M')
