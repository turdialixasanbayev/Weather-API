from rest_framework import  generics

from .serializers import RegionCreateAPISerializer
from apps.weather.models import Region
from config.permissions import IsAdminUser


class RegionCreateAPIView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionCreateAPISerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Region.objects.all().select_related('country')
