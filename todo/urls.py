from django.urls import path, reverse_lazy, include
from django.contrib.auth.decorators import login_required

from .views import TasksListView, TaskCreateView, TaskUpdateView, toggle_task, TaskDeleteView

app_name = "todo"
urlpatterns = [
    path("", login_required(TasksListView.as_view()), name="task_list"),
    path("new/", login_required(TaskCreateView.as_view()), name ="task_create"),
    path("<int:pk>/edit/", login_required(TaskUpdateView.as_view()), name="task_update"),
    path("<int:pk>/toggle/",toggle_task, name = "toggle_task"),
    path("<int:pk>/delete/", login_required(TaskDeleteView.as_view()), name = "task_delete"),
]
