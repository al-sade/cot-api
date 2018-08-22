from rest_framework import viewsets

from .models import Device, Property
from .serializers import DeviceSerializer, PropertySerializer

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.all()


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()
