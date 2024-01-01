from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
import json
from datetime import date
import base64
from django.http import JsonResponse
import base64



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



   #  employee_id = models.SmallIntegerField(primary_key=True)
  