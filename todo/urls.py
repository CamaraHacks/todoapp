from django.urls import path, reverse_lazy

from .views import TasksListView, TaskCreateView, TaskUpdateView, toggle_task, TaskDeleteView

app_name = "todo"
urlpatterns = [
    path("", TasksListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name ="task_create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/toggle/",toggle_task, name = "toggle_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name = "task_delete"),
]
