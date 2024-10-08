from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Estudantes
from escola.serializers import EstudantesSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudantes.objects.create(
            Nome = 'Teste 1',
            Email = 'Email1@gmail.com',
            CPF = '65448392563',
            Data_Nascimento = '2024-10-06',
            Celular = '71 99999-1010'
        )
        self.estudante_02 = Estudantes.objects.create(
            Nome = 'Teste 2',
            Email = 'Email2@gmail.com',
            CPF = '58842223514',
            Data_Nascimento = '2024-10-01',
            Celular = '71 99999-2020'
        )
    def testReqGetLisEstu(self):
        """Teste de requisição get para listar estudantes """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_ReqGetListarEstudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url+'/1')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudantes = Estudantes.objects.get(pk=1)
        dados_estudantes_seri = EstudantesSerializer(instance=dados_estudantes).data
        self.assertEqual(response.data,dados_estudantes_seri)

    def test_ReqPost(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            'Nome':'Testeeeee',
            'Email':'Emaillll2@gmail.com',
            'CPF':'62718986026',
            'Data_Nascimento':'2005-10-01',
            'Celular':'71 99919-2020'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_ReqDeleteEstudante(self):
        """Teste de requisição Delete para um estudante"""
        response = self.client.delete(f'{self.url}/2') #outra forma de pegar a rota
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_ReqPut(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            'Nome':'Testee',
            'Email':'Emailll02@gmail.com',
            'CPF':'16482053050',
            'Data_Nascimento':'2005-10-01',
            'Celular':'71 99919-2020'
        }
        response = self.client.put(self.url+'/1',dados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


