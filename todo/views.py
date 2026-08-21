from django.views.generic import ListView
from .models import Task

# Create your views here.


class HomePageView(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = "tasks"
    ordering = "-created_date"
