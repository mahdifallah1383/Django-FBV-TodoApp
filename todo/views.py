from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskUpdateForm
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


class TaskUpdate(UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskUpdateForm
    template_name = "update_task.html"


class DeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task-list")
    template_name = "task_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
