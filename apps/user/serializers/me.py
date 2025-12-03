from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    email = serializers.EmailField()
