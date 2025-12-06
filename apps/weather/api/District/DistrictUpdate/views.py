from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import DistrictUpdateAPISerializer
from apps.weather.models import District
from config.permissions import IsAdminUser


class DistrictUpdateAPIView(RetrieveUpdateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictUpdateAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = self.queryset.select_related('region')
        return queryset

    def perform_update(self, serializer):
        serializer.save()
