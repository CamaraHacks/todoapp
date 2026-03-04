from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from .views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.urls import reverse

class TaskTests(TestCase):
    def teste_task_belongs_to_user(self):
        user = User.objects.create_user(username ='usuario_mocado', password='senhamocada')
        task = Task.objects.create(title='task_mocada', user = user)
        self.assertEqual(task.user, user)  

    def test_is_not_a_user(self):
        url = reverse('todo:task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_is_user(self):
        user = User.objects.create_user(username="usuario_mocado", password="test123")
        self.client.login(username = 'usuario_mocado', password='test123')
        url = ''
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        user = User.objects.create_user(username="usuario_mocado", password="test123")
        self.client.login(username='usuario_mocado', password='test123')
        url = reverse('todo:task_create')
        response = self.client.post(url, {'title':'tarefa_mocada', 
                                          'priority':'medium', 'description':'só mais um mocado meu chapa'})
        self.assertEqual(response.status_code, 302)


    def test_update_view(self):
        user = User.objects.create_user(username="usuario_mocado", password="test123")
        task = Task.objects.create(title= 'tarefa_mocada', priority= 'medium', description ='só mais um mocado meu chapa', user = user)
        self.client.login(username='usuario_mocado', password='test123')
        url = reverse('todo:task_update', kwargs ={'pk': task.pk})
        response = self.client.post(url, {'title':'tarefa_mocada_atualizada', 
                                          'priority':'medium', 'description':'só mais outro mocado meu chapa'})
        self.assertEqual(response.status_code, 302)


