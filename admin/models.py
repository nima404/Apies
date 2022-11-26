from django.db import models
from django.conf import settings


class Logging(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_logs')
    model = models.CharField(max_length=220)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user} -> {self.model}'


class PriceRange(models.Model):
    min = models.IntegerField(default=0, unique=True)
    max = models.IntegerField(default=0, unique=True)
    ratio = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f'{self.min} -> |{self.ratio}| -> {self.max}'
