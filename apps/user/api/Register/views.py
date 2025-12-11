from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from ...smtp_utils import send_notification_email

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        send_notification_email(
            to=user.email,
            subject="Ro'yxatdan o'tish muvaffaqiyatli!",
            message=f"Salom {user.email}, siz muvaffaqiyatli royxatdan o'tdingiz!"
        )
