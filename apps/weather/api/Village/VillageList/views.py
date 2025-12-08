from rest_framework.generics import ListAPIView

from apps.weather.models import Village
from .serializers import VillageListAPISerializer
from config.permissions import IsAdminUser


class VillageListAPIView(ListAPIView):
    """
    This API view provides a list of all Village instances.
    """

    queryset = Village.objects.all()
    serializer_class = VillageListAPISerializer
    permission_classes = [IsAdminUser]
    pagination_class = None

    def get_queryset(self):
        queryset = self.queryset.select_related('district')
        return queryset
