from .models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'car_brand', 'car_model',
                  'production_year', 'car_body', 'engine_type']
