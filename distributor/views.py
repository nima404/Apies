from rest_framework import viewsets, views, mixins, status
from django.utils import timezone
from django.db.models import Q
from .serializers import *
from .models import *


class DistributorView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DistributorSerializer
    queryset = Distributor.objects.filter(status=1, expire_at__gt=timezone.now())

    def retrieve(self, request, pk, slug):
        obj = self.queryset.get(pk=pk, slug=slug)
        ser = DistributorRetrieveSerializer(instance=obj)
        return views.Response(ser.data)


class CategoryDistributorView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = DistributorSerializer
    queryset = Distributor.objects.filter(status=1, expire_at__gt=timezone.now())


class CategoriesDistributorView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = CategorySerializer
    queryset = BaseCategory.objects.all()
