from django.db import models
from accounts.models import Profile

# Create your models here.


class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class META:
        ordering = ["created_date"]
        order_with_respect_to = "profile"
