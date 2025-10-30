from django.urls import path, reverse_lazy

from .views import TasksListView, TaskCreateView

app_name = "todo"
urlpatterns = [
    path("", TasksListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name ="task_create"),
]
