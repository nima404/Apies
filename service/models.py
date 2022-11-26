from django.db import models
from django.conf import settings
from shop.models import BaseCategory, Category, SubCategory
from utils.funcs import product_code, product_image_path
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    class ModeChoices(models.IntegerChoices):
        physical = 1, _('physical')
        digital = 2, _('digital')

    class StatusChoices(models.IntegerChoices):
        publish = 1, _('publish')
        pending = 2, _('pending')
        dont_publish = 3, _('dont_publish')

    title = models.CharField(max_length=220)
    second_title = models.CharField(max_length=220)

    slug = models.SlugField(blank=True, max_length=500, unique=True)

    product_code = models.IntegerField(blank=True, null=True, unique=True, default=product_code)
    extra_code = models.CharField(max_length=100, null=True, blank=True)
    iran_kala_code = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='user_service',
                             on_delete=models.SET_NULL)
    password = models.CharField(max_length=110, null=True, blank=True)

    mode = models.IntegerField(choices=ModeChoices.choices, default=ModeChoices.physical)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.dont_publish)

    base_category = models.ForeignKey(BaseCategory, related_name='base_service', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_service', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='subcategory_service', on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag', related_name='service_tags')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True, blank=True)
    publish_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("distributor:distributor_solo_show", args=(self.id, self.slug))

    def __str__(self):
        return self.title


class Images(models.Model):
    service = models.ForeignKey(Service, related_name='service_images', on_delete=models.CASCADE)

    file = models.FileField(upload_to=product_image_path, validators=[
        FileExtensionValidator(
            [
                'jpg',
                'mp4'
                'png'
            ], message='This Format Not Acceptable.'
        )
    ])

    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.file.url


class Detail(models.Model):
    service = models.ForeignKey(Service, related_name='service_details', on_delete=models.CASCADE)

    title = models.CharField(max_length=120)
    value = models.CharField(max_length=220)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Size(models.Model):
    class TypeChoices(models.IntegerChoices):
        percent = 1, _('percent')
        price = 2, _('price')

    service = models.ForeignKey(Service, related_name='service_size', on_delete=models.CASCADE)
    mode = models.IntegerField(choices=TypeChoices.choices, default=TypeChoices.price)
    name = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Color(models.Model):
    class TypeChoices(models.IntegerChoices):
        percent = 1, _('percent')
        price = 2, _('price')

    service = models.ForeignKey(Service, related_name='service_colors', on_delete=models.CASCADE)
    mode = models.IntegerField(choices=TypeChoices.choices, default=TypeChoices.price)
    color = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.color


class Physical(models.Model):
    service = models.OneToOneField(Service, related_name='service_physical', on_delete=models.CASCADE)

    inventory = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}, {self.service.title}'


class Digital(models.Model):
    service = models.OneToOneField(Service, related_name='service_digital', on_delete=models.CASCADE)
    size = models.CharField(max_length=220, default="0 GB")
    parts = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}, {self.service.title}'


class DigitalProductUrl(models.Model):
    digital = models.ForeignKey(Digital, related_name='service_url', on_delete=models.CASCADE)
    url = models.URLField(max_length=900)

    objects = models.Manager()

    def __str__(self):
        return self.digital.product.title

