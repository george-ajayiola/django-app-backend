from .views import DrinksDetails, DrinksRetrieveView, CreateDrinkView, health
from django.urls import path

urlpatterns = [
    path('getDrinks', DrinksDetails.as_view(), name='drinkslist'),
    path('createDrink',CreateDrinkView.as_view(), name='createdrink'),    
    path('drinks/<pk>', DrinksRetrieveView.as_view(), name='fetch-drink'),
    path('health',health),
]