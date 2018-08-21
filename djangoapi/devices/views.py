from rest_framework import generics

from .models import Device, Property
from .serializers import DeviceSerializer, PropertySerializer

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class DeviceCreate(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceUpdate(generics.UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDelete(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class PropertyCreate(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdate(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDelete(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
