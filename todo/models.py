from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class META:
        ordering = ["created_date"]
        order_with_respect_to = "user"
