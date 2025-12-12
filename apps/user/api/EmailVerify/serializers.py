from rest_framework import serializers
from django.contrib.auth import get_user_model
from ...models import VerifyCode
import random
from apps.user.smtp_utils import send_notification_email

User = get_user_model()

class SendVerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def validate_email(self, value):
        user = self.context['request'].user
        if value != user.email:
            raise serializers.ValidationError("Sizning email manzilingiz bilan mos kelmaydi.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        code = None
        while True:
            code_candidate = f"{random.randint(100000, 999999)}"
            if not VerifyCode.objects.filter(code=code_candidate).exists():
                code = code_candidate
                break

        verify_obj = VerifyCode.objects.create(code=code)

        send_notification_email(
            subject="Email tasdiqlash kodi",
            message=f"Sizning tasdiqlash kodingiz: {code}",
            to=user.email
        )

        return verify_obj

class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True, max_length=6)

    def validate_code(self, value):
        try:
            verify_obj = VerifyCode.objects.get(code=value)
        except VerifyCode.DoesNotExist:
            raise serializers.ValidationError("Kod noto'g'ri.")

        self.context['verify_obj'] = verify_obj
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        verify_obj = self.context['verify_obj']

        user.is_verified = True
        user.save()

        verify_obj.delete()

        return user
