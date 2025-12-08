from rest_framework import serializers

from apps.user.models import MonitoringLog


class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringLog
        fields = "__all__"
