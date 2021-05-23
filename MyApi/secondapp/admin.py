from django.contrib import admin
from .models import Car


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model',
                    'production_year', 'car_body', 'engine_type')
