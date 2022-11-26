from django.contrib import admin
from django.contrib.auth.models import Group
from django.apps import apps

app = apps.get_app_config('user')
for model in app.get_models():
    admin.site.register(model)

admin.site.unregister(Group)
