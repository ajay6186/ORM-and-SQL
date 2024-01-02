from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.db import models


@api_view(['GET'])
def select_all_p(request):
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
def select_few_columns_p(request):
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


@api_view(['GET'])
def Old_price_New_price_p(request):
      with connection.cursor() as cursor:
        cursor.execute("select  product_name, unit_price as old_price, unit_price*2 as new_price  from products")
        results = cursor.fetchall()
        data_list = []
      for result in results:
            data = {
                'product_name': result[0],
                'old_price': result[1],
                'unit_price': result[2],
               
            }
            data_list.append(data)
      return Response(data_list)


# SELECT PRODUCT_NAME,

# UNIT_PRICE AS Old_Price,

# UNIT_PRICE*2 AS new_Price

# FROM PRODUCTS;
@api_view(['GET'])
def select_old_price_and_new_price(request):
    data = {'message': 'This response from SQL'}
    cursor = connection.cursor()
    cursor.execute("SELECT PRODUCT_NAME, UNIT_PRICE AS Old_Price, UNIT_PRICE*2 AS new_Price FROM products")
    result = cursor.fetchall()
    response = []
    for r in result:
        d = {}
        d['product_name'] =    r[0]
        d['Old_Price'] =    r[1]
        d['new_Price'] =    r[2]
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
