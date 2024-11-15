# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Fix: auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
