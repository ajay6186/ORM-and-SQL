from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Product, Product,Customer_p,Order,OrderDetails
import json
from datetime import date
import base64
from django.http import JsonResponse
import base64
from django.db.models import F
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.db.models import FloatField, F
from django.db.models import F, Func, Value
from django.db.models.functions import Cast
from django.db.models import F, Func, Value, FloatField 
from django.http import JsonResponse
from rest_framework import status
from django.db.models import F, ExpressionWrapper, fields
from django.db import models
from decimal import Decimal 


from django.db.models import F, ExpressionWrapper, DecimalField, IntegerField

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


def select_old_price_and_new_price_p(request):
    data = Product.objects.values('product_name').annotate(new_Price=F('unit_price')*2, Old_Price=F('unit_price')) 
    print(data)
    response = []
    for product in data:
        d = {}
        d['product_name'] = product.get('product_name')
        d['Old_price'] = product.get('Old_Price')
        d['new_price'] = product.get('new_Price')
        response.append(d)
    return JsonResponse(response, safe=False)
  
@api_view(['GET'])
def select_old_price_and_new_price(request):
    products =  Product.objects.values('product_name').annotate(new_Price=ExpressionWrapper(F('unit_price') * 2, output_field=IntegerField()), Old_Price=F('unit_price'))
    response = []
    for product in products:
       d ={}
       d['product_name']  = product.get('product_name')
       d['new_Price']  = product.get('new_Price')
       d['Old_Price']  = product.get('Old_Price')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


def select_report_with_comment_p(request): #esme comment name kam coloumn add kr diya usme value he static value our comments
    customers = Customer_p.objects.all().annotate(comment = Value('Our Comments ==>'))
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


def select_distinct_p(request):
    data= Customer_p.objects.values('country').distinct()  # remove duplicate element
    response = []
    for result in data:
        d={}
        d['country']  = result.get('country')
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


def select_distinct_p_list(request):
    data= Customer_p.objects.values('country').distinct()  # remove duplicate element
    d={}
    d['country'] = []
    for result in data:
        l  = result.get('country')
        d['country'].append(l)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)


def alias_sql_alias_p(request):  # change the coloumn name using F function
    data= Employee.objects.values('employee_id', 'first_name', 'title_of_courtesy').annotate(
        ID=F('employee_id'),
        NAME=F('first_name'),
        TITLE=F('title_of_courtesy')
    )
    response = []
    for employee in data:
       d ={}
       d['ID']  = employee.get('ID')
       d['NAME']  = employee.get('NAME')
       d['TITLE']  = employee.get('TITLE')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


def reporting_with_Concatenation_p(request): #concate the value
    data = Employee.objects.annotate(NAME=Concat('title_of_courtesy', Value(''), 'first_name')).values('NAME')
    d={}
    d['name'] = []
    for customer in data:
          l=customer.get('NAME')
          d['name'].append(l)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)


def reporting_with_concatenation_customer_location_p(request): #CONCATE static vales
    customers = Customer_p.objects.annotate(LOCATION=Concat(Value(' is from '), 'city', Value(' in '), 'country')).values('company_name', 'LOCATION')
    response = []
    for customer in customers:
       d ={}
       d['company_name']  = customer.get('company_name')
       d['LOCATION']  = customer.get('LOCATION')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


def reporting_with_concatenation_customer_location_New_p(request):
    datas = Customer_p.objects.annotate(LOCATION=Concat('company_name', Value(' is from '), 'city', Value(' in '), 'country')).values('LOCATION')
    d={}
    d['LOCATION']=[]
    for result in datas:
        data=result.get('LOCATION')
        d['LOCATION'].append(data)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)


def reporting_with_Concatenation_p(request):
    products = Product.objects.annotate(PRODUCT=F('product_name'),VALUE=Concat(Value('$'), F('unit_price') * F('units_in_stock'),output_field=CharField())).values('PRODUCT','VALUE')
    response = []
    for product in products:
       d ={}
       d['PRODUCT']  = product.get('PRODUCT')
       d['VALUE']  = product.get('VALUE')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


def report_formatting_without_concatention_p(request): # without concat orm is not working
    datas = Employee.objects.annotate(FULL_NAME=Concat(F('last_name'), Value(' '), F('first_name'), output_field=CharField())).values('FULL_NAME')
    d={}
    d['FULL_NAME']=[]
    for result in datas:
        data=result.get('FULL_NAME')
        d['FULL_NAME'].append(data)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)



def report_formatting_add_two_coloumn_in_one_coloumn_p(request):
    datas = Employee.objects.annotate(full_name=Concat(Value('FirstName: '), F('first_name'), Value('   LastName: '), F('last_name'),output_field=CharField()))
    d={}
    d['full_name']=[]
    for result in datas:
        data=result.full_name
        d['full_name'].append(data)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)


def report_formatting_add_three_coloumn_in_one_coloumn_p(request):
    employees = Employee.objects.annotate(full_name=Concat('title_of_courtesy',Value(' '), Value(' '),  'first_name',output_field=CharField()))
    d={}
    d['full_name']=[]
    for result in employees:
        data=result.full_name
        d['full_name'].append(data)
    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)



def round_amount_one_decimal(request):
    products = Product.objects.annotate(
        rounded_unit_price=models.ExpressionWrapper(
            F('unit_price'),
            output_field=DecimalField(max_digits=5, decimal_places=2)
        )
    ).values_list('rounded_unit_price', flat=True)
    
    d = {}
    d['rounded_unit_price'] = [float(result) for result in products]

    return JsonResponse(d, safe=False, status=status.HTTP_200_OK)


def round_amounformattiong_53(request):
    # products = Product.objects.annotate(value=ExpressionWrapper(F('unit_price') * F('units_in_stock'),output_field=fields.FloatField())).values('product_name','value')
    products = Product.objects.annotate(value=ExpressionWrapper(F('unit_price') * F('units_in_stock'), output_field=fields.FloatField()),formatted_value=Func(Value('$'), F('value'),function='CONCAT', output_field=CharField())).values('product_name', 'formatted_value')
    response=[]
    for product in products:
       d ={}
       d['PRODUCT']  = product.get('product_name')
       d['VALUE']  = product.get('formatted_value')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

def order_by_company_name(request):
    # SELECT * FROM CUSTOMERS ORDER BY COMPANY_NAME
    data=Customer_p.objects.all().order_by('company_name')
    response=[]
    for product in data:
       d ={}
       d['customer_id']  = product.customer_id
       d['company_name']  = product.company_name
       d['contact_name']  = product.contact_name
       d['contact_title']  = product.contact_title
       d['address']  = product.address
       d['city']  = product.city
       d['region ']  = product.region 
       d['postal_code']  = product.postal_code
       d['country']  = product.country
       d['phone']  = product.phone
       d['fax']  = product.fax
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)



def order_by_customer_id_asc_order_id_desc(request):
    orders = Order.objects.all().order_by('customer', '-order_id')
    response=[]
    for order in orders:
       d ={}
       d['order_id']  = order.order_id
       d['customer_id']  = order.customer_id
       d['employee_id']  = order.employee_id
       d['order_date']  = order.order_date
       d['required_date']  = order.required_date
       d['shipped_date']  = order.shipped_date
       d['ship_via']  = order.ship_via_id 
       d['freight']  = order.freight
       d['ship_name']  = order.ship_name 
       d['ship_address']  = order.ship_address
       d['ship_city']  = order.ship_city
       d['ship_region']  = order.ship_region 
       d['ship_postal_code']  = order.ship_postal_code
       d['ship_country']  = order.ship_country
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)



def order_by_customer_id_asc_order_id_asc(request):
    orders = Order.objects.all().order_by('customer', 'order_id')
    response=[]
    for order in orders:
       d ={}
       d['order_id']  = order.order_id
       d['customer_id']  = order.customer_id
       d['employee_id']  = order.employee_id
       d['order_date']  = order.order_date
       d['required_date']  = order.required_date
       d['shipped_date']  = order.shipped_date
       d['ship_via']  = order.ship_via_id 
       d['freight']  = order.freight
       d['ship_name']  = order.ship_name 
       d['ship_address']  = order.ship_address
       d['ship_city']  = order.ship_city
       d['ship_region']  = order.ship_region 
       d['ship_postal_code']  = order.ship_postal_code
       d['ship_country']  = order.ship_country
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def where_sales_manager_details(request):
    title=request.POST.get('title')
    employees = Employee.objects.filter(title=title)
    response = []
    for employee in employees:
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


def where_owner_details(request):
    customers = Customer_p.objects.filter(contact_title='Owner').values('company_name', 'contact_title', 'address', 'city', 'country', 'phone')
    response = []
    for customer in customers:
       d ={}
       d['company_name']  = customer.get('company_name')
       d['contact_title']  = customer.get('contact_title')
       d['address']  = customer.get('address')
       d['city']  = customer.get('city')
       d['country']  = customer.get('country')
       d['phone']  = customer.get('phone')
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def where_specific_order_id(request):
    order_id=request.POST.get('order_id')
    orders = Order.objects.filter(order_id=order_id)
    response=[]
    for order in orders:
       d ={}
       d['order_id']  = order.order_id
       d['customer_id']  = order.customer_id
       d['employee_id']  = order.employee_id
       d['order_date']  = order.order_date
       d['required_date']  = order.required_date
       d['shipped_date']  = order.shipped_date
       d['ship_via']  = order.ship_via_id 
       d['freight']  = order.freight
       d['ship_name']  = order.ship_name 
       d['ship_address']  = order.ship_address
       d['ship_city']  = order.ship_city
       d['ship_region']  = order.ship_region 
       d['ship_postal_code']  = order.ship_postal_code
       d['ship_country']  = order.ship_country
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def where_searching_product(request):
        unit_price=int(request.POST.get('unit_price'))
        product_name=request.POST.get('product_name')
       
        prod = Product.objects.filter(product_name=product_name, unit_price=unit_price)
        response=[]
        for product in prod:
            d ={}
            d['PRODUCT_NAME']  = product.product_name
            d['UNIT_PRICE']  = product.unit_price
            response.append(d)
        return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def where_searching_for_customer_id(request):
        customer_id=request.POST.get('customer_id')
        company_name=request.POST.get('company_name')
        customers =Customer_p.objects.filter(customer_id=customer_id,company_name=company_name)
        response = []
        for customer in customers:
            d ={}
            d['customer_id']  = customer.customer_id
            d['company_name']  = customer.company_name
            response.append(d)
        return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_product_above(request):
    unit_price = request.POST.get('unit_price')
    result = Product.objects.filter(unit_price__gt=unit_price).order_by('unit_price').values('product_name', 'unit_price')
    response = []
    for res in result:
            d ={}
            d['product_name']  = res.get('product_name')
            d['unit_price']  = res.get('unit_price')
            response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_product_less(request):
    unit_price = request.POST.get('unit_price')
    result = Product.objects.filter(unit_price__lt=unit_price).order_by('unit_price').values('product_name', 'unit_price')
    response = []
    for res in result:
            d ={}
            d['product_name']  = res.get('product_name')
            d['unit_price']  = res.get('unit_price')
            response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_product_whose_price_are_40_above(request):
    unit_price = request.POST.get('unit_price')
    result = Product.objects.filter(unit_price__gte=unit_price).order_by('unit_price').values('product_name', 'unit_price')
    response = []
    for res in result:
            d ={}
            d['product_name']  = res.get('product_name')
            d['unit_price']  = res.get('unit_price')
            response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_product_with_range(request):
    order_id_1 = request.POST.get('order_id_1')
    order_id_2 = request.POST.get('order_id_2')
    orders = Order.objects.filter(order_id__lt=order_id_1) | Order.objects.filter(order_id__gt=order_id_2)
    response=[]
    for order in orders:
       d ={}
       d['order_id']  = order.order_id
       d['customer_id']  = order.customer_id
       d['employee_id']  = order.employee_id
       d['order_date']  = order.order_date
       d['required_date']  = order.required_date
       d['shipped_date']  = order.shipped_date
       d['ship_via']  = order.ship_via_id 
       d['freight']  = order.freight
       d['ship_name']  = order.ship_name 
       d['ship_address']  = order.ship_address
       d['ship_city']  = order.ship_city
       d['ship_region']  = order.ship_region 
       d['ship_postal_code']  = order.ship_postal_code
       d['ship_country']  = order.ship_country
       response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_product_rostocking(request):
    units_in_stock = request.POST.get('units_in_stock')
    reorder_level = request.POST.get('reorder_level')
    products = Product.objects.filter(units_in_stock__lt=units_in_stock, reorder_level__gt=reorder_level).order_by('units_in_stock')

    response = []
    for product in products:
        d = {
            'product_name': product.product_name,
            'units_in_stock': product.units_in_stock,
            'reorder_level': product.reorder_level,
        }
        response.append(d)

    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def order_amount_of_10540_or_above(request):
    unit_price = request.POST.get('unit_price')
    quantity = request.POST.get('quantity')
    # data = OrderDetails.objects.filter(Amount__gte=10540.00).annotate(Amount=ExpressionWrapper(F('unit_price') * F('quantity'), output_field=DecimalField())).order_by('-Amount','order_id')
    data = OrderDetails.objects.filter(unit_price__gte=Decimal(unit_price),quantity__gte=int(quantity)).annotate(Amount=ExpressionWrapper(F('unit_price') * F('quantity'), output_field=DecimalField())).order_by('-Amount', 'order_id')
    response = []
    for result in data:
        d = {
            'order_id': result.order_id,
            'Amount': result.Amount,
        }
        response.append(d)

    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def where_not_mr(request):
    title_of_courtesy=request.POST.get('title_of_courtesy')
    employees = Employee.objects.exclude(title_of_courtesy=title_of_courtesy)
    response = []
    for employee in employees:
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


@api_view(['POST'])
def where_not_sales_representative(request):
    title=request.POST.get('title')
    employees = Employee.objects.exclude(title=title)
    response = []
    for employee in employees:
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


@api_view(['POST'])
def where_price_between_two_figure(request):
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    products = Product.objects.filter(unit_price__gte=min_price,unit_price__lte=max_price).order_by('unit_price','product_name')
    response = []
    for product in products:
        d = {
            'product_name': product.product_name,
            'units_price': product.unit_price,
        }
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)    


@api_view(['POST'])
def where_price_not_between_two_figure(request):
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    products = Product.objects.exclude(unit_price__gte=min_price,unit_price__lte=max_price).order_by('unit_price','product_name')
    response = []
    for product in products:
        d = {
            'product_name': product.product_name,
            'units_price': product.unit_price,
        }
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)  


@api_view(['POST'])
def where_two_between(request):
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    min_price_1 = request.POST.get('min_price_1')
    max_price_1 = request.POST.get('max_price_1')
    products = Product.objects.filter(unit_price__range=(min_price, max_price)).filter(unit_price__range=(max_price_1, min_price_1)).order_by('unit_price')
    response = []
    for product in products:
        d = {
            'product_name': product.product_name,
            'units_price': product.unit_price,
        }
        response.append(d)
    return JsonResponse(response, safe=False, status=status.HTTP_200_OK) 




    



   









































   