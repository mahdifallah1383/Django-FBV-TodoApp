from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("create/", TaskCreate.as_view(), name="create-task"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="update-task"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="complete-task"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete-task"),
]
