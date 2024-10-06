from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')

    def testAutCredCert(self):
        """
        Teste destinado a verificar se com as credencias certas, a autenticação é feita
        """
        usuario = authenticate(username = 'admin',password = 'admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def testAutCredIncert(self):
        """
        Teste destinado a verificar se com as credencias incorretas no username, a autenticação é feita
        """
        usuario = authenticate(username = 'adm',password = 'admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def testAutCredIncertSenha(self):
        """
        Teste destinado a verificar se com as credencias incorretas na senha, a autenticação é feita
        """
        usuario = authenticate(username = 'admin',password = 'adm')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def testReqGetCer(self):
        """Teste para verificar uma requisição GET se autorizada ou não"""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


