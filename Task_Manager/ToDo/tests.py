from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

User = get_user_model()

class ToDoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.force_login(self.user)
        self.task = Task.objects.create(
            description='Test Task',
            status=Task.TODO,
            user=self.user
        )

    def get_jwt_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_task_list_create_view(self):
        token = self.get_jwt_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post('/api/task_manager/tasks/', {'description': 'New Task'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('error', response.data)
        self.assertFalse(response.data['error'])
        self.assertIn('objeto', response.data)

    def test_task_detail_view(self):
        token = self.get_jwt_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(f'/api/task_manager/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('error', response.data)
        self.assertFalse(response.data['error'])
        self.assertIn('objeto', response.data)
        self.assertEqual(response.data['objeto']['description'], 'Test Task')
