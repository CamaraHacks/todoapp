from django.urls import path, reverse

from .views import TasksListView, TaskCreateView

app_name = "todo"
urlpatterns = [
    path("", TasksListView.as_view(), name="Tasks"),
    path("new/", TaskCreateView.as_view(), name ="task_create"),
]
