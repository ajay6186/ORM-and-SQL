from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.http import JsonResponse

@api_view(['GET'])
def select_all(request):
    data = {'message': 'This response from SQL'}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    response = []
    for r in result:
        d = {}
        d['employee_id'] =    r[0]
        d['last_name'] =    r[1]
        d['first_name'] =    r[2]
        d['title'] =    r[3]
        d['title_of_courtesy'] =    r[4]
        d['birth_date'] =    r[5].strftime('%Y-%m-%d')
        d['hire_date'] =    r[6].strftime('%Y-%m-%d')
        d['address'] =    r[7]
        d['city'] =    r[8]
        d['region'] =    r[9]
        d['postal_code'] =    r[10]
        d['country'] =    r[11]
        d['home_phone'] =    r[12]
        d['extension'] =    r[13]
        d['photo'] =    r[14].tobytes().decode('utf-8')  if isinstance(r[14], str) else None,
        d['notes'] =    r[15]
        d['reports_to'] =    r[16] if r[16] else None
        d['photo_path'] =    r[17]
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_few_columns(request):
    data = {'message': 'This response from SQL'}
    cursor = connection.cursor()
    cursor.execute("SELECT first_name, last_name, address, country FROM employees")
    result = cursor.fetchall()
    response = []
    for r in result:
        d = {}
        d['first_name'] =    r[0]
        d['last_name'] =    r[1]
        d['address'] =    r[2]
        d['country'] =    r[3]
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)