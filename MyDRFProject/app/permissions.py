from rest_framework.permissions import BasePermission


class IsProjectOwner(BasePermission):
    """
    Only project owner can modify the project or create tasks in it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
