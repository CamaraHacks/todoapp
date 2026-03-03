from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from .views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.urls import reverse_lazy

class TaskTests(TestCase):
    def teste_task_belongs_to_user(self):
        user = User.objects.create_user(username ='usuario_mocado', password='senhamocada')
        task = Task.objects.create(title='task_mocada', user = user)
        self.assertEqual(task.user, user)  

    def test_title_max_lenght(self):
        user = User.objects.create_user(username="usuario_mocado", password="test123")
        task = Task.objects.create(title="a" * 200, user=user)
        self.assertEqual(len(task.title), 200)

    def is_not_a_user(self):
        url = reverse('todo:task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_is_user(self):
        user = User.objects.create_user(username="usuario_mocado", password="test123")
        self.client.login(username = 'usuario_mocado', password='test123')
        url = ''
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
