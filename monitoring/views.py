from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from apps.user.models import MonitoringLog

from .serializers import MonitoringSerializer


class MonitoringAPIView(APIView):
    def get(self, request):
        logs = MonitoringLog.objects.all()
        return Response(MonitoringSerializer(logs, many=True).data, status=status.HTTP_200_OK)
