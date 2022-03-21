from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Task
from django.contrib.auth.models import User

# Create your tests here.
class TestListCreateTodos(APITestCase):

    def create_task(self):
        sample_task = { 
            "title": "Test", 
            "description": "Testing test",
            "due_date": "2022-03-20", 
            "task_state": "TODO"
        }
        return sample_task

    def authenticate(self):
        self.user = User.objects.create_superuser(
            username = 'username',
            email = 'username@gmail.com',
            password = 'password'
        )
        self.client.force_login(user=self.user)

    def test_should_not_create_task_with_no_auth(self):
        response = self.client.post(reverse("task-view", kwargs={'pk': 1}), self.create_task())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_create_task(self):
        self.authenticate()
        response = self.client.post(reverse("task-view", kwargs={'pk': 1}), self.create_task())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_return_all_tasks(self):
        self.authenticate()
        response = self.client.get(reverse("task-view", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_change_existing_task(self):
        self.authenticate()
        response = self.client.patch(reverse("task-view", kwargs={'pk': 1}), self.create_task())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_should_delete_existing_task(self):
        self.authenticate()
        response = self.client.delete(reverse("task-view", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    