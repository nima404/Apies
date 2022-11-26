from rest_framework import serializers
from .models import User, Address
from django.conf import settings
from json import loads, load

r = settings.R


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def create(self, validated_data):
        user = self.context['user']
        old = validated_data['old_password']
        new = validated_data['new_password']
        if user.check_password(old) and old != new:
            user.set_password(new)
            user.save(update_fields=['password'])
        return validated_data


class OTPCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=8)

    def validate(self, data):
        if r_data := r.get(data['code']).decode():
            return {'code': r_data}
        return data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone',
            'password',
        )

    def save(self):
        user = User.objects.create_user(
            phone=self.validated_data.get('phone'),
            password=self.validated_data.get('password'),
            role=self.context.get('role')
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'phone',
            'mail',
            'image',
            'company_name',
            'gender',
        ]

