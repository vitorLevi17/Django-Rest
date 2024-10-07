from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Curso
from rest_framework import status
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