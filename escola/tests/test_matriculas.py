from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Matricula, Estudantes, Curso
from rest_framework import status
class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)

        self.matricula1 = Matricula.objects.create(
            id_estudante = Estudantes.objects.create(
            Nome = 'Teste 1',
            Email = 'Email1@gmail.com',
            CPF = '65448392563',
            Data_Nascimento = '2024-10-06',
            Celular = '71 99999-1010'
        ),
            id_curs = Curso.objects.create(
            id_curso = 'POO',
            Descricao = 'Programacao orientada a Objetos',
            Nivel = 'B'
        ),
            periodo = "M"
        )

        self.matricula2 = Matricula.objects.create(
            id_estudante= Estudantes.objects.create(
                Nome = 'Teste 2',
                Email = 'Email2@gmail.com',
                CPF = '58842223514',
                Data_Nascimento = '2024-10-01',
                Celular = '71 99999-2020'
        ),
            id_curs= Curso.objects.create(
                id_curso='PY',
                Descricao='Programacao Python',
                Nivel='I'
        ),
            periodo="N"
        )
    def testReqGetListMatr(self):
        """Teste de requisição get para listar matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)