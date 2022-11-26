from rest_framework import serializers
from .models import *


class DistributorSerializer(serializers.ModelSerializer):
    base_category = serializers.CharField(source='base_category.name')
    category = serializers.CharField(source='category.name')
    sub_category = serializers.CharField(source='sub_category.name')
    user = serializers.CharField(source='user.full_name')
    url = serializers.URLField(source='get_absolute_url')
    price = serializers.IntegerField(source='distributor_price.price')
    images = serializers.ListSerializer(child=serializers.URLField(source='url'), source='distributor_images')

    class Meta:
        model = Distributor
        exclude = (
            "mode",
            "password",
            "extra_code",
            "updated_at",
            "slug",
            "tags",
            "status",
            "iran_kala_code",
            "description",
            "publish_at",
            "created_at"
        )


class DigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digital
        fields = (
            "size",
            "parts"
        )


class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical
        fields = (
            "inventory",
            "weight",
            "length",
            "width",
            "height"
        )


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = (
            "title",
            "value"
        )


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'color',
            'mode',
            'value'
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'name',
            'mode',
            'value'
        )


class DistributorRetrieveSerializer(serializers.ModelSerializer):
    base_category = serializers.CharField(source='base_category.name')
    category = serializers.CharField(source='category.name')
    sub_category = serializers.CharField(source='sub_category.name')
    user = serializers.CharField(source='user.full_name')
    tags = serializers.ListSerializer(child=serializers.CharField(source='name'))
    images = serializers.ListSerializer(child=serializers.URLField(source='url'), source='distributor_images')
    digital = DigitalSerializer(source='distributor_digital')
    physical = PhysicalSerializer(source='distributor_physical')

    details = DetailSerializer(many=True, source='distributor_details')

    price = serializers.CharField(source='distributor_price.price')

    color = ColorSerializers(many=True, source='distributor_colors')
    size = SizeSerializer(many=True, source='distributor_size')

    class Meta:
        model = Distributor
        exclude = (
            "mode",
            "password",
            "extra_code",
            "updated_at",
            "slug",
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseCategory
        fields = [
            'id',
            'name'
        ]
