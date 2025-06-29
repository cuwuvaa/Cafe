from django.urls import path
from . import views


app_name = "tasks"
urlpatterns=[
    path("", views.list_tasks, name="list"),
    path("add_task", views.add_task, name="add")
]