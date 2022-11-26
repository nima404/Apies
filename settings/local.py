from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

OTP = {
    'username': '09130666144',
    'password': '831#6d4fO',
    'number': '50004001666144'
}

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
