from rest_framework.generics import RetrieveDestroyAPIView

from apps.weather.models import Village
from .serializers import VillageDeleteAPISerializer
from config.permissions import IsAdminUser


class VillageDeleteAPIView(RetrieveDestroyAPIView):
    """
    This API view allows retrieving and deleting a specific Village instance.
    """

    queryset = Village.objects.all()
    serializer_class = VillageDeleteAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Village.objects.select_related('district')
        return queryset

    def perform_destroy(self, instance):
        # Custom deletion logic can be added here if needed
        instance.delete()
