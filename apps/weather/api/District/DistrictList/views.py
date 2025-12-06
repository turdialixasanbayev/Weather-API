from rest_framework.generics import ListAPIView

from .serializers import DistrictListAPISerializer
from apps.weather.models import District
from config.permissions import IsAdminUser


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListAPISerializer
    permission_classes = [IsAdminUser]
    pagination_class = None

    def get_queryset(self):
        queryset = self.queryset.select_related('region')
        return queryset
