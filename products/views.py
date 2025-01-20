from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def health(request):
    return Response({"Status":'Healthy'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def myapi(request):
    return Response("Hello world!!, this is my API product", status=status.HTTP_200_OK)