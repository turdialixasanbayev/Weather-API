from rest_framework.generics import RetrieveAPIView

from .serializers import DistrictRetrieveAPISerializer
from apps.weather.models import District
from config.permissions import IsAdminUser


class DistrictRetrieveAPIView(RetrieveAPIView):
    """
    This view retrieves a single District instance.
    """
    queryset = District.objects.all()
    serializer_class = DistrictRetrieveAPISerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = District.objects.all().select_related('region')
        return queryset
