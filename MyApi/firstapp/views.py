from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CarSpecsSerializer
from .models import CarSpec, CarPlan


@api_view()
@permission_classes([AllowAny])
def first_function(request):
    print(request.query_params)
    print(request.query_params['id'])
    number = request.query_params['id']
    new_number = int(number) * 2
    return Response({"message": "We received your request", "result": new_number})


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpec.objects.all()
        return car_specs

    def retrieve_car(self, request, *args, **kwargs):
        params = kwargs
        params_list = params['pk'].split('-')
        cars = CarSpec.objects.filter(
            car_brand=params_list[0], car_model=params_list[1])
        serializer = CarSpecsSerializer(cars, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data
        new_car = CarSpec.objects.create(car_plan=CarPlan.objects.get(id=car_data['car_plan']), car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                                         production_year=car_data['production_year'], car_body=car_data['car_body'], engine_type=car_data['engine_type'])
        new_car.save()
        serializer = CarSpecsSerializer(new_car)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logged_in = request.user
        if logged_in == 'admin':
            car = self.get_object()
            car.delete()
            response_message = {"message": "data has been deleted"}
        else:
            response_message = {"message": "operation is not allowed"}
        return Response(response_message)
