from django.db import models


class CarPlan(models.Model):
    plan_name = models.CharField(max_length=20)
    year_of_warranty = models.PositiveBigIntegerField(default=1)
    finance_plan = models.CharField(max_length=20, default='unavailable')

    def __str__(self):
        return f"{self.plan_name}"


class CarSpec(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.car_model} of {self.car_brand}"
