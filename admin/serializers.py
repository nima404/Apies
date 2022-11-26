from rest_framework import serializers
from distributor.models import (
    Distributor,
    Tag,
    Images,
    Price,
    Detail,
    Size,
    Color,
    Physical,
    Digital
)
from shop.models import SubCategory, BaseCategory, Category


class ImageDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ('created_at',)
        extra_kwargs = {
            'product': {'write_only': True},
        }


class DetailDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        exclude = ()
        extra_kwargs = {
            'product': {
                'write_only': True
            }
        }


class SizeDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class ColorDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class PhysicalDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class DigitalDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digital
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class PriceDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class TagDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ()
        extra_kwargs = {
            'product': {'write_only': True},
        }


class DistributorSerializer(serializers.ModelSerializer):
    images = ImageDistributorSerializer(source='distributor_images', many=True, read_only=True)
    details = DetailDistributorSerializer(source='distributor_details', many=True, read_only=True)
    sizes = SizeDistributorSerializer(source='distributor_size', many=True, read_only=True)
    colors = ColorDistributorSerializer(source='distributor_colors', many=True, read_only=True)
    physical = PhysicalDistributorSerializer(source='distributor_physical', allow_null=True, read_only=True)
    digital = DigitalDistributorSerializer(source='distributor_digital', allow_null=True, read_only=True)
    price = PriceDistributorSerializer(source='distributor_price', read_only=True)

    class Meta:
        model = Distributor
        exclude = ()
        extra_kwargs = {
            'slug': {'read_only': True},
            'user': {'read_only': True, 'required': True, 'allow_null': False},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(DistributorSerializer, self).create(validated_data)


# End Distributor

class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCategory
        exclude = ()
        # extra_kwargs = {}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
        # extra_kwargs = {}


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ()
        # extra_kwargs = {}


class FullSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ()
        # extra_kwargs = {}


class FullCategorySerializer(serializers.ModelSerializer):
    sub_category = FullSubCategorySerializer(many=True)

    class Meta:
        model = Category
        exclude = ()
        # extra_kwargs = {}


class FullBaseCategorySerializer(serializers.ModelSerializer):
    category = FullCategorySerializer(many=True)

    class Meta:
        model = BaseCategory
        exclude = ()
        # extra_kwargs = {}
