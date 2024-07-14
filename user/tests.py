from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class UserSignupViewTestCode(APITestCase):
    def test_signup(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'password': 'testuserpassword',
            'email': 'testuser@test.com',
            'signature': '홍길동',
            'phone': '01012341234'
        }

        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
