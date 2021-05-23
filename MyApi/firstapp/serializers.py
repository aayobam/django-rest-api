from .models import CarSpec
from rest_framework import serializers


class CarSpecsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarSpec
        fields = ['id', 'car_plan', 'car_brand', 'car_model',
                  'production_year', 'car_body', 'engine_type']
