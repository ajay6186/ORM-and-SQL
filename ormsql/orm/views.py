from django.shortcuts import render

# Create your views here.
 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @api_view(['GET'])
# def your_api_view(request):
#     data = {'message': 'Hello, this is a JSON response from a function-based view!'}
#     return Response(data, status=status.HTTP_200_OK)
@api_view(['GET'])
def ajay_orm_test(request):
    data = {'message': 'Hello, this is a JSON response from a function-based view!'}
    return Response(data, status=status.HTTP_200_OK) 