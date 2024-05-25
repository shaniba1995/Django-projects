from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_name=models.CharField(max_length=150)
    todo_desc=models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)