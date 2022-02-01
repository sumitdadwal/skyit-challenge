from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializer import CarSerializer
from firstcarapi.models import Car

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    return Response({'message': 'Success'})

class CarViewset(viewsets.ModelViewSet):
    serializer_class = CarSerializer

    def get_queryset(self):
        cars = Car.objects.all()
        return cars

    def put(self, request, *args, **kwargs):
        car_object = Car.objects.get()

        data = request.data

        car_object.mileage = data['mileage']
        car_object.updated = data['updated']

        car_object.save()

        serailizer = CarSerializer(car_object)
        return Response(serailizer.data)
