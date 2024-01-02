from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Products
import json
from datetime import date
import base64
from django.http import JsonResponse
import base64
from django.db.models import F



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


def Old_price_New_price_p(request):
   #  data =  Products.objects.values('product_name','unit_price').annotate(Old_Price = F('unit_price'))
    data = Products.objects.values('product_name').annotate(new_Price=F('unit_price')*2, Old_Price=F('unit_price')) 
    print(data)
    response = []
    for product in data:
        d = {}
        d['product_name'] = product.get('product_name')
        d['Old_price'] = product.get('Old_Price')
        d['new_price'] = product.get('new_Price')
        response.append(d)
    return JsonResponse(response, safe=False)



    
