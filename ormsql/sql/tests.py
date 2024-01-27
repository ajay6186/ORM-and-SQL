# from django.test import TestCase

# # Create your tests here.
# @api_view(['GET'])
# def ajay_orm_test(request):
#     data = {'message': 'Hello, this is a sql query'}
#     return Response(data, status=status.HTTP_200_OK) 


# @api_view(['GET'])
# def fetch_data(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM actor")
#         results = cursor.fetchall()
#         data_list = []
#     for result in results:
#         data = {
#             'actor_id': result[0],
#             'first_name': result[1],
#             'last_name': result[2],
#             'last_update': result[3],
#         }
#         data_list.append(data)
#     return Response(data_list)


# @api_view(['GET'])
# def adress_data(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM address")
#         results = cursor.fetchall()
#         data_list = []
#     for result in results:
#         data = {
#             'address_id': result[0],
#             'address': result[1],
#             'address2': result[2],
#             'district': result[3],
#             'city_id': result[4],
#             'postal_code': result[5],
#             'phone': result[6],
#             'last_update': result[7],
#         }
#         data_list.append(data)
#     return Response(data_list)


# from django.db import connection
# from django.http import JsonResponse
# from rest_framework import status
# from rest_framework.decorators import api_view

# @api_view(['POST'])
# def order_amount_of_10540_or_above(request):
#     order_id = request.POST.get('order_id')
#     unit_price = request.POST.get('unit_price')

#     cursor = connection.cursor()

#     # Build SQL query dynamically
#     query = "SELECT order_id, unit_price * quantity AS Amount FROM order_details WHERE"

    # # Check if order_id is provided
    # if order_id:
    #     query += f" order_id = {order_id} AND"

    # # Check if unit_price is provided
    # if unit_price:
    #     query += f" unit_price * quantity >= {unit_price} AND"

    # # Remove the trailing 'AND' if it exists
    # if query.endswith("AND"):
    #     query = query[:-3]

    # # Add ORDER BY clause
    # query += " ORDER BY Amount DESC"

    # # Execute the query
    # cursor.execute(query)
    
    # data = cursor.fetchall()
    # response = []
    # for result in data:
    #     d = {
    #         'order_id': result[0],
    #         'Amount': result[1],
    #     }
    #     response.append(d)

    # return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@api_view(['POST'])
@csrf_exempt
def where_two_between(request):
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')

    cursor = connection.cursor()

    query = "SELECT PRODUCT_NAME, UNIT_PRICE FROM PRODUCTS WHERE UNIT_PRICE BETWEEN %s AND %s OR UNIT_PRICE BETWEEN %s AND %s ORDER BY UNIT_PRICE"
    cursor.execute(query, [min_price, max_price, '50', '53'])

    data = cursor.fetchall()

    response = []
    for result in data:
        d = {
            'product_name': result[0],
            'unit_price': result[1],
        }
        response.append(d)

    return JsonResponse(response, safe=False)


