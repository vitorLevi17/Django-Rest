from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from escola.models import Estudantes

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 =Estudantes.objects.create(
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