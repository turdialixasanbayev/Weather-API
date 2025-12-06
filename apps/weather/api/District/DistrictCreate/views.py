from rest_framework.generics import CreateAPIView

from .serializers import DistrictCreateAPISerializer
from apps.weather.models import District
from config.permissions import IsAdminUser


class DistrictCreateAPIView(CreateAPIView):
    """
    This view allows admin users to create new District entries.
    """

    queryset = District.objects.all()
    serializer_class = DistrictCreateAPISerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = District.objects.all().select_related('region')
        return queryset

    def perform_create(self, serializer):
        serializer.save()
