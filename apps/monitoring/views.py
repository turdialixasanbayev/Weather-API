from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MonitoringLog
from .serializers import MonitoringSerializer
from config.permissions import IsAdminUser

class MonitoringAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            logs = MonitoringLog.objects.all()
            return Response(
                MonitoringSerializer(logs, many=True).data,
                status=status.HTTP_200_OK,
            )
        except MonitoringLog.DoesNotExist:
            return Response(
                {"detail": "No monitoring logs found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        finally:
            from django.db import connection
            connection.close()
