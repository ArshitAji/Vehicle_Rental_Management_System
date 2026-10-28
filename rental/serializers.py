from rest_framework import serializers
from rental.models import *

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehicleDb
        fields="__all__"
        read_only_fields=["id"]
class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerDb
        fields="__all__"
        read_only_fields=["id"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingDb
        fields="__all__"
        read_only_fields=["id","booking_date"]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentDb
        fields="__all__"
        read_only_fields=["id","payement_date"]