from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.


class TasksListView(ListView):
    model = Task
    template_name = "todo/task_list.html"

class TaskCreateView(CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("task_list")
