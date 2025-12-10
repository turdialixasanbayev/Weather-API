from rest_framework import serializers
from .models import MonitoringLog

class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringLog
        fields = "__all__"
