from django.db import models

# Create your models here.
class Task(models.Model):
    task_head = models.CharField(max_length=30)
    task_dres = models.TextField()
    def __str__(self):
        return self.task_head