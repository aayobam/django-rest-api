from django.contrib import admin
from .models import CarSpec, CarPlan


@admin.register(CarSpec)
class AdminCarSpec(admin.ModelAdmin):
    list_display = ('car_plan', 'car_brand', 'car_model',
                    'production_year', 'car_body', 'engine_type')


@admin.register(CarPlan)
class AdminCarPlan(admin.ModelAdmin):
    list_display = ('plan_name', 'year_of_warranty', 'finance_plan')
