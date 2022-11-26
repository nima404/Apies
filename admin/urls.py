from django.urls import path
from .routers import router

app_name = 'admin'

urlpatterns = [

] + router.urls
