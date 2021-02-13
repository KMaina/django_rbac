from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import (CustomerRegistrationSerializer,
                          AttendantRegistrationSerializer)
from django_rba.utility.permissions import IsAdminOrAttendant


class CustomerRegistration(APIView):
    permission_classes = [IsAdminOrAttendant]
    serializer_class = CustomerRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = {
            'message': 'User registered successfully',
            }
        return Response(message, status=status.HTTP_201_CREATED)


class AttendantRegistration(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = AttendantRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = {
            'message': 'User registered successfully',
            }
        return Response(message, status=status.HTTP_201_CREATED)
