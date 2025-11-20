from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # Search by project name
    def get_queryset(self):
        queryset = Project.objects.all()
        search = self.request.query_params.get("search")
        owner = self.request.query_params.get("owner")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if owner:
            queryset = queryset.filter(owner=owner)

        return queryset


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        status = self.request.query_params.get("status")
        project_id = self.request.query_params.get("project_id")
        due_before = self.request.query_params.get("due_before")

        if status:
            queryset = queryset.filter(status=status)

        if project_id:
            queryset = queryset.filter(project_id=project_id)

        if due_before:
            queryset = queryset.filter(due_date__lte=due_before)

        return queryset


# summary-view-anchor
class DashboardViewSet(viewsets.ViewSet):

    def list(self, request):
        owner = request.query_params.get("owner")

        if not owner:
            return Response({"error": "Please provide owner=? in query parameters"})

        projects = Project.objects.filter(owner=owner)
        tasks = Task.objects.filter(project__owner=owner)

        status_summary = (
            tasks.values("status")
            .annotate(count=Count("status"))
            .order_by()
        )

        upcoming = tasks.filter(
            status__in=["todo", "in_progress"],
            due_date__isnull=False
        ).order_by("due_date")[:5]

        upcoming_data = (
            TaskSerializer(upcoming, many=True).data
            if upcoming.exists()
            else "No upcoming tasks!"
        )

        return Response({
            "total_projects": projects.count(),
            "total_tasks": tasks.count(),
            "status_summary": status_summary,
            "upcoming_tasks": upcoming_data
        })
