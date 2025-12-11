from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendVerifyCodeSerializer, VerifyCodeSerializer
from config.permissions import IsAuthenticatedAndIsUnVerified
from django.shortcuts import redirect

class SendVerifyCodeView(APIView):
    permission_classes = [IsAuthenticatedAndIsUnVerified]
    serializer_class = SendVerifyCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Verification code sent to your email."},
            status=status.HTTP_200_OK
        ) # DRF
        # return redirect('verify-code') # Django

class VerifyCodeView(APIView):
    permission_classes = [IsAuthenticatedAndIsUnVerified]
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Email verified successfully."},
            status=status.HTTP_200_OK
        ) # DRF
        # return redirect('me') # Django
