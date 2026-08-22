from django import forms
from django.forms import ModelForm
from .models import Task


class AddTaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)

    class Meta:
        model = Task
        fields = ["title"]
