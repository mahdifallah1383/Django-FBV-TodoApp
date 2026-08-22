from django.views.generic import ListView, CreateView
from .models import Task
from .forms import AddTaskForm
from django.urls import reverse_lazy

# Create your views here.


class TaskList(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = "tasks"
    ordering = "-created_date"


class TaskCreate(CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
