from . import views
from django.urls import path

urlpatterns = [
    path('health',views.health),
    path('myapi',views.myapi),
]