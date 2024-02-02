from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthJWTTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def get_jwt_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_token_obtain_pair_view(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('error', response.data)
        self.assertFalse(response.data['error'])
        self.assertIn('objeto', response.data)
        self.assertIn('access', response.data['objeto'])
        self.assertIn('refresh', response.data['objeto'])
