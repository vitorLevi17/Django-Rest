from django.test import TestCase
from escola.models import Estudantes,Curso

class FixturesTestCase(TestCase):
    fixtures = ["prototipoBanco.json"]

    def test_carregamentoFix(self):
        """Teste pra ver carregamento de fixtures"""
        estudante = Estudantes.objects.get(CPF="34567890110")
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.Celular,"71 93243-2323")
        self.assertEqual(curso.id_curso,"POO")
