from django.contrib import admin
from .models import Project, Task
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id","name","description","owner"]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","project","title"]