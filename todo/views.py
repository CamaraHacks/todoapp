from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task



@login_required
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
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "priority"]
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title","priority", "description","completed"]
    success_url = reverse_lazy("todo:task_list")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task_list")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

