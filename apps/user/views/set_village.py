from rest_framework.generics import UpdateAPIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from ..serializers.set_village import UserSetVillageSerializer


class UserSetVillageAPIView(UpdateAPIView):
    serializer_class = UserSetVillageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        village = user.village

        return Response(
            {
                "message": "Manzil muvaffaqiyatli o'zgartirildi!",
                "location": {
                    "country": village.district.region.country.name,
                    "region": village.district.region.name,
                    "district": village.district.name,
                    "village": village.name,
                },
            },
            status=status.HTTP_200_OK,
        )
