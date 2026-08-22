from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("create/", TaskCreate.as_view(), name="create-task"),
]
