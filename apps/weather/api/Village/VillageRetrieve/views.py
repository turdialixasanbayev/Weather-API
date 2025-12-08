from rest_framework.generics import RetrieveAPIView

from apps.weather.models import Village
from .serializers import VillageDetailAPISerializer
from config.permissions import IsAdminUser


class VillageDetailAPIView(RetrieveAPIView):
    """
    This API view retrieves detailed information about a specific Village instance.
    """

    queryset = Village.objects.all()
    serializer_class = VillageDetailAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Village.objects.select_related('district')
        return queryset
