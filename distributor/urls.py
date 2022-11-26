from django.urls import path
from .views import DistributorView, CategoryDistributorView, CategoriesDistributorView

app_name = 'distributor'

urlpatterns = [
    path('shop/<int:pk>/<str:slug>/', DistributorView.as_view({'get': 'retrieve'}), name='distributor_solo_show'),
    path('shop/list/<int:base_category>/<int:category>/<int:sub_category>/',
         CategoryDistributorView.as_view({'get': 'list'}), name='distributor_category'),
    path('shop/list/', DistributorView.as_view({'get': 'list'})),
    path('shop/categories/', CategoriesDistributorView.as_view({'get': 'list'}))
]
