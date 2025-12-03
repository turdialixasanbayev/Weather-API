from rest_framework.generics import RetrieveAPIView

from .serializers import RegionDetailAPISerializer

from apps.weather.models import Region
from config.permissions import IsAdminUser


class RegionDetailAPIView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Region.objects.all().select_related('country')
        return queryset
