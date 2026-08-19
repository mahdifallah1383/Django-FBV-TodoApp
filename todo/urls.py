from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("", HomePageView.as_view(), name="todo-home"),
]
