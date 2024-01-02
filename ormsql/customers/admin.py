from django.contrib import admin
from customers.models import Customers
# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'company_name','contact_name','contact_title') 
admin.site.register(Customers, CustomersAdmin)