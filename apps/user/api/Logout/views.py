from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from config.permissions import IsAuthenticated
from .serializers import LogoutSerializer
from ...smtp_utils import send_notification_email

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_email = serializer.validated_data.get("email", None)
        refresh_token = serializer.validated_data.get("refresh", None)
        send_notification_email(
            to=user_email,
            subject="Logout muvaffaqqiyatli amalga oshirildi",
            message=f"{user_email}, siz tizimdan muvaffaqiyatli chiqdingiz! Sizning refresh_token: {refresh_token} bloklandi"
        )
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
