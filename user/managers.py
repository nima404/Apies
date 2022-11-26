from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given phone must be set')

        user = self.model(phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone=None, password=None, role=7, **extra_fields):
        extra_fields.setdefault('role', role)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('role', 1)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('role') is not 1:
            raise ValueError('Superuser must have role=1.')

        return self._create_user(phone, password, **extra_fields)
