from django.shortcuts import render

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'

