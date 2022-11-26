from django.db import models
from .managers import UserManager
from django.utils.translation import gettext_lazy as _
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.hashers import (
    check_password,
    make_password,
)
from uuid import uuid5, NAMESPACE_URL


class User(models.Model):

    def user_dir(self, filename: str) -> str:
        return f'{uuid5(NAMESPACE_URL, str(self.id))}/profile/{filename}'

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('male')
        FEMALE = 'F', _('female')

    class RoleChoices(models.IntegerChoices):
        OWNER = 1, _('owner')
        TOTAL_ADMIN = 2, _('total admin')
        USUAL_ADMIN = 3, _('usual admin')
        SELLER = 4, _('seller')
        SERVICE = 5, _('service')
        DISTRIBUTOR = 6, _('distributor')
        WRITER = 7, _('writer')
        USER = 8, _('user')

    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, validators=[])
    mail = models.EmailField(max_length=220, blank=True, null=True, unique=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=80, null=True, blank=True)
    website = models.URLField(max_length=400, null=True, blank=True)
    image = ProcessedImageField(upload_to=user_dir, max_length=255, default='default/img.jpg',
                                processors=[ResizeToFill(500, 500)], format='JPEG', options={'quality': 50})

    company_name = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=150, default='iran')
    state = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    national_code = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True, null=True)
    introduction = models.CharField(max_length=180, null=True, blank=True)
    role = models.IntegerField(choices=RoleChoices.choices, default=RoleChoices.USER)
    wallet = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=False)

    password = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = [
        'full_name'
    ]

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        if self.role == 1:
            return True
        return False

    def has_perm(self, perm, obj=None):
        if self.role == 1:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.role == 1:
            return True
        return False

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'user'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_addresses')
    postal_code = models.CharField(max_length=120)
    address = models.TextField()

    def __str__(self):
        return self.user.phone

    class Meta:
        db_table = 'Address'
