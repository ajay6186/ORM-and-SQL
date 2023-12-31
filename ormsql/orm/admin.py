from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name','last_name','title','title_of_courtesy', 'birth_date') 
admin.site.register(Employee, EmployeeAdmin)