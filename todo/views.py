from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Task

# Create your views here.
def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    if task.completed:
        task.completed_date = timezone.now()
    task.save()
    return redirect('todo:task_list')


class TasksListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    fields = ["created_date", "priority"]

    def get_queryset(self):
        return Task.objects.all().order_by('completed', '-created_date')

class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "priority"]
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task_list")

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title","priority", "description","completed"]
    success_url = reverse_lazy("todo:task_list")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task_list")
    

