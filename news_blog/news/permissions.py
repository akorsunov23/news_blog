from rest_framework import permissions

class CheckingPermissions(permissions.BasePermission):
    """
    Проверить, является ли аутентифицированный пользователь автором сообщения или админом.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_superuser