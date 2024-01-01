from django.db import models

# Create your models here.
# myapp/models.py

class Employee(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, null=True, blank=True)
    title_of_courtesy = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=15, null=True, blank=True)
    region = models.CharField(max_length=15, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    home_phone = models.CharField(max_length=24, null=True, blank=True)
    extension = models.CharField(max_length=4, null=True, blank=True)
    photo = models.BinaryField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_column='reports_to')
    photo_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.first_name


from django.db import models

from django.db import models

class Categories(models.Model):
    category_id = models.SmallIntegerField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    picture = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'categories'
        unique_together = ['category_id', 'category_name']

# If you want to define constraints explicitly, you can use the `unique_together` attribute in the Meta class.

# Example:
# class Meta:
#     db_table = 'categories'
#     unique_together = ['category_id', 'category_name']

class Suppliers(models.Model):
    supplier_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, null=True, blank=True)
    contact_title = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=15, null=True, blank=True)
    region = models.CharField(max_length=15, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=24, null=True, blank=True)
    fax = models.CharField(max_length=24, null=True, blank=True)
    homepage = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'suppliers'
        unique_together = ['supplier_id', 'company_name']

# If you want to define constraints explicitly, you can use the `unique_together` attribute in the Meta class.

# Example:
# class Meta:
#     db_table = 'suppliers'
#     unique_together = ['supplier_id', 'company_name']


class Product(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    product_name = models.CharField(max_length=40)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    quantity_per_unit = models.CharField(max_length=20, null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    units_in_stock = models.SmallIntegerField(null=True, blank=True)
    units_on_order = models.SmallIntegerField(null=True, blank=True)
    reorder_level = models.SmallIntegerField(null=True, blank=True)
    discontinued = models.IntegerField()

    class Meta:
        db_table = 'products'
        unique_together = ['product_id', 'product_name']

# If you want to define constraints explicitly, you can use the `unique_together` attribute in the Meta class.

# Example:
# class Meta:
#     db_table = 'products'
#     unique_together = ['product_id', 'product_name']

