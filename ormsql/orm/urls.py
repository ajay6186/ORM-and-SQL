from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('select_all/', select_all),
    path('field_data/', field_data_p),
]
