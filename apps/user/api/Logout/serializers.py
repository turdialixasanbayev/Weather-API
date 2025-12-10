from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True, required=True)

    default_error_messages = {
        "invalid_token": "Refresh token is invalid or expired"
    }

    def save(self, **kwargs):
        try:
            refresh_token = self.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            self.fail("invalid_token")
