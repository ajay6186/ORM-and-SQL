from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('select_all/', select_all),
    path('select_few_columns/', select_few_columns),
    path('select_all_p/', select_all_p),
    path('select_few_columns_p/', select_few_columns_p),
    path('Old_price_New_price_p/', Old_price_New_price_p),
    path('select_old_price_and_new_price/', select_old_price_and_new_price),
]
