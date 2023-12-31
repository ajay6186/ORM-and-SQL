from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Product
import json
from datetime import date
import base64
from django.http import JsonResponse
import base64
from django.db.models import F, ExpressionWrapper, DecimalField, IntegerField
from customers.models import Customers
from django.db.models import Value

@api_view(['GET'])
def select_all(request):
    data = Employee.objects.all()
    response = []
    for employee in data:
        d={}
        d['employee_id']=employee.employee_id
        d['last_name'] = employee.last_name
        d['first_name'] = employee.first_name
        d['title'] = employee.title
        d['title_of_courtesy'] = employee.title_of_courtesy
        d['birth_date'] = employee.birth_date
        d['hire_date'] = employee.hire_date
        d['address'] = employee.address
        d['city'] = employee.city
        d['region'] = employee.region
        d['postal_code'] = employee.postal_code
        d['country'] = employee.country
        d['home_phone'] = employee.home_phone
        d['extension'] = employee.extension
        d['photo'] = employee.photo.tobytes().decode('utf-8')  if isinstance(employee.photo, str) else None,
        d['notes'] = employee.notes
        d['reports_to'] = employee.reports_to.employee_id if employee.reports_to else None
        d['photo_path'] = employee.photo_path
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_all_p(request):
    data = Employee.objects.all()
    response = []
    for employee in data:
        d={}
        d['employee_id']=employee.employee_id
        d['last_name'] = employee.last_name
        d['first_name'] = employee.first_name
        d['title'] = employee.title
        d['title_of_courtesy'] = employee.title_of_courtesy
        d['birth_date'] = employee.birth_date
        d['hire_date'] = employee.hire_date
        d['address'] = employee.address
        d['city'] = employee.city
        d['region'] = employee.region
        d['postal_code'] = employee.postal_code
        d['country'] = employee.country
        d['home_phone'] = employee.home_phone
        d['extension'] = employee.extension
        d['photo'] = employee.photo.tobytes().decode('utf-8')  if isinstance(employee.photo, str) else None,
        d['notes'] = employee.notes
        d['reports_to'] = employee.reports_to.employee_id if employee.reports_to else None
        d['photo_path'] = employee.photo_path
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_few_columns_p(request):
    data = Employee.objects.all().values_list('first_name','last_name','address','country')
    response = []
    for employee in data:
         d={}
         d['first_name'] = employee[0]
         d['last_name'] = employee[1]
         d['address'] = employee[2]
         d['country'] = employee[3]
         response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_few_columns(request):
    data = Employee.objects.values('first_name', 'last_name', 'address', 'country')
    response = []
    for employee in data:
       d ={}
       d['first_name']  = employee.get('first_name')
       d['last_name']  = employee.get('last_name')
       d['title_of_courtesy']  = employee.get('title_of_courtesy')
       d['address']  = employee.get('address')
       d['country']  = employee.get('country')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_old_price_and_new_price(request):
    products = Product.objects.values('product_name').annotate(new_Price=ExpressionWrapper(F('unit_price') * 2, output_field=IntegerField()), Old_Price=F('unit_price'))
    response = []
    for product in products:
       d ={}
       d['product_name']  = product.get('product_name')
       d['new_Price']  = product.get('new_Price')
       d['Old_Price']  = product.get('Old_Price')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_report_with_comment(request):
    customers = Customers.objects.all().annotate(comment = Value('Our Comments ==>'))
    response = []
    for customer in customers:
       d ={}
       d['comment']  = customer.comment
       d['customer_id']  = customer.customer_id
       d['company_name']  = customer.company_name
       d['contact_name']  = customer.contact_name
       d['contact_title']  = customer.contact_title
       d['address']  = customer.address
       d['city']  = customer.city
       d['region']  = customer.region
       d['postal_code']  = customer.postal_code
       d['country']  = customer.country
       d['phone']  = customer.phone
       d['fax']  = customer.fax

       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_distinct(request):
    # DISTINCT ==> remove duplicate
    customers = Customers.objects.values('country').distinct()
    response_dict = {}
    response_dict['country'] = []
    for customer in customers:
        response_dict['country'].append(customer.get('country'))
    return JsonResponse(response_dict, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def select_distinct_list(request):
    # DISTINCT ==> remove duplicate
    customers = Customers.objects.values('country').distinct()
    response_list = list(customers)
    return JsonResponse(response_list, safe=False, status=status.HTTP_200_OK)

from django.db import models
@api_view(['GET'])
def alias_sql_alias(request):
    employees_data = Employee.objects.values(ID=models.F('employee_id'), NAME=models.F('first_name'),TITLE=models.F('title_of_courtesy'))
    response_list = list(employees_data)
    return JsonResponse(response_list, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def alias_sql_alias_comprihention(request):
    employees_data = Employee.objects.annotate(ID=F('employee_id'), NAME=F('first_name'), TITLE=F('title_of_courtesy')).values('ID','NAME','TITLE')
    response_list = list(employees_data)
    return JsonResponse(response_list, safe=False, status=status.HTTP_200_OK)

from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
@api_view(['GET'])
def reporting_with_concatenation(request):
    employees_data = Employee.objects.annotate(NAME=Concat('title_of_courtesy',Value(' '),'first_name',Value(' '),'last_name',output_field=CharField())).values('NAME')
    # data = list(employees_data)
    data = []
    for employee in employees_data:
        d ={}
        d['NAME'] = employee.get('NAME')
        data.append(d)
    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

# from django.db import connection
# for query in connection.queries:
#     print(query['sql'])
#     print("Time:", query['time'])
#     print()
# from django.db import connection
# for query in connection.queries:
#     print(query['sql'])
#     print("Time:", query['time'])
#     print()