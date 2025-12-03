from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import RegionUpdateAPISerializer

from apps.weather.models import Region
from config.permissions import IsAdminUser


class RegionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionUpdateAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        return Region.objects.all().select_related('country')
