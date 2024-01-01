from django.contrib import admin
from django.urls import path
from sql.views import *
urlpatterns = [
    path('select_all/',select_all),
    
]
