from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Matricula, Estudantes, Curso
from rest_framework import status
from escola.serializers import MatriculaSerializer
class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudantes.objects.create(
            Nome='Estudante',
            Email='estudante@gmail.com',
            CPF='03998874070',
            Data_Nascimento='2003-02-02',
            Celular='11 98765-4321'
        )
        self.curso = Curso.objects.create(
            id_curso='CTT', Descricao='Curso Teste', Nivel='B'
        )
        self.estudante2 = Estudantes.objects.create(
            Nome='Estudanteeeeeeeee',
            Email='estudanteeeeeeee@gmail.com',
            CPF='42896082050',
            Data_Nascimento='2013-02-02',
            Celular='11 98865-4321'
        )
        self.curso2 = Curso.objects.create(
            id_curso='GO', Descricao='Curso de go', Nivel='A'
        )

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
        """Teste de requisição PUT para um estudante"""
        dados = {
            'id_estudante':self.estudante2.pk,
            'id_curso':self.curso2.pk,
            'Nivel':'A',
        }
        response = self.client.put(self.url+'/1',dados)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
