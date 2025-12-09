from rest_framework import viewsets

from .serializers import WeatherSerializer

from apps.weather.models import Weather
from config.permissions import IsAdminUser


class WeatherViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Weather objects."""
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
    pagination_class = None  # Disable pagination for this viewset
    filterset_class = None  # No filterset class specified

    def get_queryset(self):
        """Retrieve the queryset of Weather objects."""
        return self.queryset.select_related('village')

    def perform_create(self, serializer):
        """Create a new Weather object."""
        serializer.save()

    def perform_update(self, serializer):
        """Update an existing Weather object."""
        serializer.save()

    def perform_destroy(self, instance):
        """Delete a Weather object."""
        instance.delete()

    def get_object(self):
        """Retrieve a specific Weather object by its primary key."""
        return super().get_object()

    def get_serializer_class(self):
        """Return the serializer class for this viewset."""
        return self.serializer_class

    def get_permissions(self):
        """Return the list of permissions for this viewset."""
        return [permission() for permission in self.permission_classes]

    def get_lookup_field(self):
        """Return the lookup field for this viewset."""
        return self.lookup_field

    def get_pagination_class(self):
        """Return the pagination class for this viewset."""
        return self.pagination_class

    def get_filterset_class(self):
        """Return the filterset class for this viewset."""
        return self.filterset_class
