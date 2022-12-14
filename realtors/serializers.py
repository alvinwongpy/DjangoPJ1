from rest_framework import serializers
from .models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ['name', 'phone', 'enail', 'hire_date']
