from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('select_all/',select_all),
    path('select_few_columns/',select_few_columns),
]
