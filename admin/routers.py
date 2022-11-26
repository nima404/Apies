from rest_framework import routers
from .views import DistributorView, ImagesDistributorView, DetailDistributorView, ColorDistributorView, \
    SizeDistributorView, PhysicalDistributorView, DigitalDistributorView, PriceDistributorView, TagDistributorView, \
    FullCategoryView

router = routers.DefaultRouter()

router.register('distributor', DistributorView, basename='distributor')
router.register('distributor-images', ImagesDistributorView, basename='distributor-images'),
router.register('distributor-details', DetailDistributorView, basename='distributor-details')
router.register('distributor-color', ColorDistributorView, basename='distributor-color')
router.register('distributor-size', SizeDistributorView, basename='distributor-size')
router.register('distributor-physical', PhysicalDistributorView, basename='distributor-physical')
router.register('distributor-digital', DigitalDistributorView, basename='distributor-digital')
router.register('distributor-price', PriceDistributorView, basename='distributor-price')
router.register('distributor-tag', TagDistributorView, basename='distributor-')
router.register('category-base-category', FullCategoryView, basename='category-base-category')