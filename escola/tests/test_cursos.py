from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Curso
from rest_framework import status
from escola.serializers import CursoSerializer
class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso1 = Curso.objects.create(
            id_curso = 'POO',
            Descricao = 'Programacao orientada a Objetos',
            Nivel = 'B'
        )
        self.curso2 = Curso.objects.create(
            id_curso='PY',
            Descricao='Programacao Python',
            Nivel='I'
        )
    def testReqGetListCurso(self):
        """Teste de requisição get para listar cursos """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def reqGetCurso(self):
        """Teste de requisição GET para um curso"""
        response = self.client.get(self.url+'/2')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=2)
        dados_curso_seri = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data,dados_curso_seri)

    def test_reqPostCurso(self):
        """Teste de requisição POST para um curso"""
        dados = {
            'id_curso':'PHP',
            'Descricao':'Curso de PHP para web',
            'Nivel':'I'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_ReqDeleteCurso(self):
        """Teste de requisição Delete para um curso"""
        response = self.client.delete(f'{self.url}/1') #outra forma de pegar a rota
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_ReqPutCurso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            'id_curso':'Java',
            'Descricao':'Curso de java para ambiente web',
            'Nivel':'A',
        }
        response = self.client.put(self.url+'/1',dados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)





