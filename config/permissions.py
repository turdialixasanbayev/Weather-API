from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Faqat aktiv admin va staff foydalanuvchilarga ruxsat beradi.
    """

    message = "Sizda bu resursga kirish ruxsati yo'q."

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_active and
            request.user.is_staff and
            request.user.is_superuser
        )
