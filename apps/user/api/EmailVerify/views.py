from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendVerifyCodeSerializer, VerifyCodeSerializer
from config.permissions import IsAuthenticatedAndIsUnVerified

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
            {
                "detail": "Verification code sent to your email.",
                "status": "success",
                "code_sent": True,
                "email": serializer.validated_data.get('email'),
                "redirect_to": "http://127.0.0.1:8000/api/user/verify-code/",
            },
            status=status.HTTP_200_OK,
        )

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
            {
                "detail": "User verified successfully.",
                "status": "success",
                "is_verified": True,
                "redirect_to": "http://127.0.0.1:8000/api/user/me/",
            },
            status=status.HTTP_200_OK,
        )
