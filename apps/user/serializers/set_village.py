from rest_framework import serializers

from ..models import CustomUser


class UserSetVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['village']
