from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car


class CarsApiView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        cars = Car.objects.all()
        return cars

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                car = Car.objects.filter(id=id)
                serializer = CarSerializer(car, many=True)
                return Response(serializer.data)
        except:
            cars = self.get_queryset()
            serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data
        new_car = Car.objects.create(car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                                     production_year=car_data['production_year'], car_body=car_data['car_body'],
                                     engine_type=car_data['engine_type'])
        new_car.save()
        serializer = CarSerializer(new_car)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.query_params["id"]
        car = Car.objects.get(id=id)
        car.delete()
        return Response({"message": "object deleted successfully"})
