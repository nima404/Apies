from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Form(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=240)

    objects = models.Manager()

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        return super().save(**kwargs)

    def __str__(self):
        return self.title
