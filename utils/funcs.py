from uuid import uuid5, NAMESPACE_URL
from melipayamak import Api
from django.conf import settings
from random import randint
from re import match
from rest_framework.serializers import ValidationError


def send_sms(phone: str, otp: str):
    text = f"""Website C2
code: {otp}
    """
    print("up")
    api = Api(settings.OTP['username'], settings.OTP['password'])
    return api.sms('rest').send(phone, settings.OTP['number'], text)


def product_code():
    return randint(0000000000, 9999999999)


def product_image_path(self, filename: str) -> str:
    return f'{uuid5(NAMESPACE_URL, str(self.id))}/images/{filename}'


def product_file_path(self, filename: str) -> str:
    return f'{uuid5(NAMESPACE_URL, str(self.id))}/{filename}'


def phone_number_validator(value):
    if not match("09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", value):
        raise ValidationError('phone number wrong ...')
