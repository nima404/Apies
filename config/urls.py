from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('admin.urls')),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('product/', include('shop.urls')),
    path('service/', include('service.urls')),
    path('distributor/', include('distributor.urls'))
]
