from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'c2oo.ir',
    '*'
]

DEBUG = False

OTP = {
    'username': '09130666144',
    'password': '831#6d4fO',
    'number': '50004001666144'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cooir_riooc',
        'USER': 'cooir_root',
        'PASSWORD': 'Uq[z9hDcBYm1cI_kCl#tD@uO',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
