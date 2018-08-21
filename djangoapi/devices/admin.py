from django.contrib import admin

from .models import Device, Property

admin.site.register([Device, Property])
