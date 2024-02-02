from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UsersTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.force_login(self.user)  # No es necesario JWT para estas pruebas

    def get_jwt_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)
    
    def test_user_registration_view(self):
        self.client.logout()
        response = self.client.post('/api/task_manager/register/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('error', response.data)
        self.assertFalse(response.data['error'])
        self.assertIn('objeto', response.data)

    def test_user_detail_view(self):
        token = self.get_jwt_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/api/task_manager/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('error', response.data)
        self.assertFalse(response.data['error'])
        self.assertIn('objeto', response.data)
        self.assertEqual(response.data['objeto']['username'], 'testuser')
