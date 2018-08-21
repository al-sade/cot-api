from rest_framework import serializers
from . import models

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Property
        fields = '__all__'
