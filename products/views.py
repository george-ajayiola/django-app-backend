from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
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