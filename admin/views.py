from rest_framework import views, viewsets, status, mixins, permissions
from distributor.models import Distributor, Images, Detail, Color, Physical, Size, Digital, Price, Tag
from shop.models import SubCategory, Category, BaseCategory
from .serializers import (DistributorSerializer, ImageDistributorSerializer, DetailDistributorSerializer,
                          ColorDistributorSerializer, PhysicalDistributorSerializer, SizeDistributorSerializer,
                          DigitalDistributorSerializer, PriceDistributorSerializer, TagDistributorSerializer,
                          CategorySerializer, SubCategorySerializer,
                          FullBaseCategorySerializer)
from user.permissions import IsTotalAdmin


class DistributorView(viewsets.ModelViewSet):
    serializer_class = DistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Distributor.objects.all()


class ImagesDistributorView(viewsets.ModelViewSet):
    serializer_class = ImageDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Images.objects.all()


class DetailDistributorView(viewsets.ModelViewSet):
    serializer_class = DetailDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Detail.objects.all()

    def create(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return views.Response(ser.data, status=status.HTTP_201_CREATED)


class ColorDistributorView(viewsets.ModelViewSet):
    serializer_class = ColorDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Color.objects.all()

    def create(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return views.Response(ser.data, status=status.HTTP_201_CREATED)


class PhysicalDistributorView(viewsets.ModelViewSet):
    serializer_class = PhysicalDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Physical.objects.all()


class DigitalDistributorView(viewsets.ModelViewSet):
    serializer_class = DigitalDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Digital.objects.all()


class SizeDistributorView(viewsets.ModelViewSet):
    serializer_class = SizeDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Size.objects.all()


class PriceDistributorView(viewsets.ModelViewSet):
    serializer_class = PriceDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Price.objects.all()


class TagDistributorView(viewsets.ModelViewSet):
    serializer_class = TagDistributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Tag.objects.all()


# End Distributor


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = Category.objects.all()


class SubCategoryView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = SubCategory.objects.all()


class FullCategoryView(viewsets.ModelViewSet):
    serializer_class = FullBaseCategorySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsTotalAdmin
    ]
    queryset = BaseCategory.objects.all()
