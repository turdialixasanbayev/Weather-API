from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import timedelta

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    remember_me = serializers.BooleanField(default=False, write_only=True, required=False)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        remember_me = attrs.get("remember_me", False)

        if not email or not password:
            raise serializers.ValidationError("Email va parol kiritilishi shart.")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Email yoki parol noto'g'ri.")

        refresh = RefreshToken.for_user(user)

        if remember_me:
            refresh.set_exp(lifetime=timedelta(days=7))
            access_token = refresh.access_token
            access_token.set_exp(lifetime=timedelta(hours=1))
        else:
            access_token = refresh.access_token

        attrs["access"] = str(access_token)
        attrs["refresh"] = str(refresh)

        return attrs
