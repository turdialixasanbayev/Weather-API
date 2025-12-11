from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from ...smtp_utils import send_notification_email
from ...utils import get_client_ip, get_ip_location

class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.validated_data.get("email", None)
        access_token = serializer.validated_data.get("access", None)
        refresh_token = serializer.validated_data.get("refresh", None)
        client_ip = get_client_ip(request)
        location = get_ip_location(client_ip)
        country = location.get("country")
        city = location.get("city")
        org = location.get("org")
        send_notification_email(
            to=user_email,
            subject="Login amalga oshirildi",
            message=(
                f"Salom {user_email}!\n\n"
                f"Akkauntingizga yangi login aniqlandi.\n\n"
                f"🔹 IP manzil: {client_ip}\n"
                f"🔹 Davlat: {country}\n"
                f"🔹 Shahar: {city}\n"
                f"🔹 Provayder (ISP): {org}\n\n"
                f"Access Token: {access_token}\n"
                f"Refresh Token: {refresh_token}\n\n"
                "Agar bu siz bo'lmasangiz, darhol parolingizni o'zgartiring!"
            )
        )
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
