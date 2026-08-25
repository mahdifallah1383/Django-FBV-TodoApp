from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Task
from .forms import TaskUpdateForm
from django.urls import reverse_lazy

# Create your views here.


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "index.html"
    context_object_name = "tasks"
    ordering = "-created_date"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskUpdateForm
    template_name = "update_task.html"


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task-list")
    template_name = "task_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:task-list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        if object.complete:
            object.complete = False
        else:
            object.complete = True

        object.save()
        return redirect(self.success_url)
