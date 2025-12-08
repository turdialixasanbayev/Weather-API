from rest_framework.generics import RetrieveUpdateAPIView

from apps.weather.models import Village
from .serializers import VillageUpdateAPISerializer
from config.permissions import IsAdminUser


class VillageUpdateAPIView(RetrieveUpdateAPIView):
    """
    This API view allows retrieving and updating a specific Village instance.
    """

    queryset = Village.objects.all()
    serializer_class = VillageUpdateAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = self.queryset.select_related('district')
        return queryset

    def perform_update(self, serializer):
        # Custom update logic can be added here if needed
        serializer.save()
