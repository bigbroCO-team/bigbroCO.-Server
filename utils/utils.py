from django.urls import reverse
from rest_framework import status

from user.models import User


def testcode_basic_authentication(self):
    self.user = User.objects.create_user(username='testuser', password='testpassword')
    url = reverse('login')
    response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.token = response.data['access']
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)


def testcode_admin_authentication(self):
    self.user = User.objects.create_superuser(username='admin', password='admin')
    url = reverse('login')
    response = self.client.post(url, {'username': 'admin', 'password': 'admin'}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.token = response.data['access']
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
