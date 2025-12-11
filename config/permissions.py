from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Faqat admin foydalanuvchilarga ruxsat beradi.
    """

    message = "Sizda bu amalni bajarish uchun yetarli huquqlar yo'q."

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_active and
            request.user.is_staff and
            request.user.is_superuser
        )


class IsAuthenticated(BasePermission):
    """
    Faqat autentifikatsiyadan o'tgan va aktiv foydalanuvchilarga ruxsat beradi.
    """

    mesage = "Siz tizimga kirishingiz kerak."

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and 
            request.user.is_active
        )


class IsAuthenticatedAndIsUnVerified(BasePermission):
    """
    Faqat autentifikatsiyadan o'tgan, aktiv va tasdiqlanmagan foydalanuvchilarga ruxsat beradi.
    """

    message = "Siz bu APIni quyidagi sabablardan biriga ko'ra ishlata olmaysiz: tizimga kirmadingiz, hisobingiz faol emas yoki tasdiqlangan."

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and 
            request.user.is_active and
            not request.user.is_verified
        )
