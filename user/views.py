from rest_framework import views, viewsets, mixins, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response
from random import randint
from .models import User
from .serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer, OTPCodeSerializer
from utils.funcs import send_sms
from django.conf import settings
from json import dumps, loads
from datetime import timedelta

r = settings.R


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsAuthenticated
    ]

    def update(self, request, *args, **kwargs):
        ser = self.serializer_class(request.user, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        ser = self.serializer_class(request.user)
        return Response(ser.data, status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data, context={'user': self.request.user})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(status=status.HTTP_200_OK)


class PreRegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [
        AllowAny
    ]

    def create(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        otp_code = str(randint(1111, 9999))
        if r.setex(otp_code, timedelta(minutes=10), value=dumps(ser.data)):
            resp = send_sms(ser.data['phone'], otp_code)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    serializer_class = OTPCodeSerializer
    permission_classes = [
        AllowAny
    ]

    def create(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        new_ser = RegisterSerializer(data=loads(ser.data['code']), context={'role': 7})
        new_ser.is_valid(raise_exception=True)
        new_ser.save()
        return Response(status=status.HTTP_200_OK)
