from django.urls import path
from .views import MonitoringAPIView

urlpatterns = [
    path("logs/", MonitoringAPIView.as_view(), name="monitoring-logs"),
]
