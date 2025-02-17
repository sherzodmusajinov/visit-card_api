from rest_framework import serializers

class VisitCardDataSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    pochta = serializers.CharField(max_length=255)
    manzil = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    name_company = serializers.CharField(max_length=255)
