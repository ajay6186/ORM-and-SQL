from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.db import models


@api_view(['GET'])
def select_all(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees")
        results = cursor.fetchall()
        data_list = []
    for result in results:
        data = {
            'employee_id': result[0],
            'last_name': result[1],
            'first_name': result[2],
            'title': result[3],
            'title_of_courtesy': result[4],
            'birth_date': result[5],
            'hire_date': result[6],
            'address': result[7],
            'city': result[8],
            'region': result[9],
            'postal_code': result[10],
            'country': result[11],
            'home_phone': result[12],
            'extension': result[13],
            'photo': result[14],
            'notes': result[15],
            'reports_to': result[16],
            'photo_path': result[17],
        }
        data_list.append(data)
    return Response(data_list)



@api_view(['GET'])
def field_data_p(request):
      with connection.cursor() as cursor:
        cursor.execute("SELECT first_name, last_name, address, country from employees")
        results = cursor.fetchall()
        data_list = []
      for result in results:
            data = {
                'first_name': result[0],
                'last_name': result[1],
                'address': result[2],
                'country': result[3],
            }
            data_list.append(data)
      return Response(data_list)


