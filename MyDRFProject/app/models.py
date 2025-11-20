from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=100)   # Removed ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("owner", "name")  # same owner cannot repeat project name

    def __str__(self):
        return f"{self.name} ({self.owner})"


class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.IntegerField()
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Validation rules
    def clean(self):
        if not (1 <= self.priority <= 5):
            raise ValidationError("Priority must be between 1 (highest) and 5 (lowest).")

        if self.status == "done" and self.due_date and self.due_date > timezone.now().date():
            raise ValidationError("A completed task cannot have a future due date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
