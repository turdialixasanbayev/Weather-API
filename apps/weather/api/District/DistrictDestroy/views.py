from rest_framework.generics import RetrieveDestroyAPIView

from .serializers import DistrictDestroyAPISerializer
from apps.weather.models import District
from config.permissions import IsAdminUser


class DistrictDestroyAPIView(RetrieveDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictDestroyAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('region')

    def perform_destroy(self, instance):
        instance.delete() # Soft delete can be implemented here if needed
