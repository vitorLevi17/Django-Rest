from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Matricula, Estudantes, Curso
from rest_framework import status
from escola.serializers import MatriculaSerializer
class MatriculasTestCase(APITestCase):
    fixtures = ["prototipoBanco.json"]
    def setUp(self):

        self.usuario = User.objects.get(username = 'vitorlevi')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudantes.objects.get(pk = 3)
        self.curso = Curso.objects.get(pk=2)
        self.estudante2 = Estudantes.objects.get(pk=4)
        self.curso2 = Curso.objects.get(pk=13)
        self.matricula1 = Matricula.objects.get(pk=1)

    def testReqGetListMatr(self):
        """Teste de requisição get para listar matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testReqGetMatri(self):
        """Teste de requisição GET para uma matricula"""
        response = self.client.get(self.url+'/1')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_matriculas = Matricula.objects.get(pk=1)
        dados_matriculas_seri = MatriculaSerializer(instance=dados_matriculas).data
        self.assertEqual(response.data,dados_matriculas_seri)

    def testReqPostMatri(self):
        """Teste de requisição POST para uma matricula"""
        dados = {
            'id_estudante': self.estudante.pk,
            'id_curs': self.curso.pk,
            'periodo':'M'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_ReqDeleteMatricula(self):
        """Teste de requisição Delete para uma matricula"""
        response = self.client.delete(f'{self.url}/1') #outra forma de pegar a rota
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_ReqPut(self):
        """Teste de requisição PUT para matricula"""
        dados = {
            'id_estudante':self.estudante2.pk,
            'id_curso':self.curso2.pk,
            'Nivel':'A',
        }
        response = self.client.put(self.url+'/1',dados)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
