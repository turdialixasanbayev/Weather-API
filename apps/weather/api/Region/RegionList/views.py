from rest_framework.generics import ListAPIView

from .serializers import RegionListAPISerializer

from apps.weather.models import Region
from config.permissions import IsAdminUser


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListAPISerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.select_related('country')
