from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer



class DrinksDetails(ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class CreateDrinkView(CreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinksRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

@api_view(['GET'])
def health(request):
    return Response({"Status":'Healthy'}, status=status.HTTP_200_OK)