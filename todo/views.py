from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.


class TasksListView(ListView):
    model = Task
    template_name = "todo/task_list.html"

    def get_query_set(self):
        return Task.objects.filter(done=False)

class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description"]
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task_list")

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "done"]
    success_url = reverse_lazy("todo:task_list")
