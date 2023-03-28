from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text
