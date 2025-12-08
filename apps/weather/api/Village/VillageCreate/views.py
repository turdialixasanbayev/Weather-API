from rest_framework.generics import CreateAPIView

from apps.weather.models import Village
from .serializers import VillageCreateAPISerializer
from config.permissions import IsAdminUser


class VillageCreateAPIView(CreateAPIView):
    """
    This API view allows creating a new Village instance.
    """

    queryset = Village.objects.all()
    serializer_class = VillageCreateAPISerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.select_related('district')

    def perform_create(self, serializer):
        # Custom create logic can be added here if needed
        serializer.save()
