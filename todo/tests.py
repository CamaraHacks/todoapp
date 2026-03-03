from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def teste_task_belongs_to_user(self):
        user = User.objects.create_user(username ='usuario_mocado', password='senhamocada')
        task = Task.objects.create(title='task_mocada', user = user)
        self.assertEqual(task.user, user)  
