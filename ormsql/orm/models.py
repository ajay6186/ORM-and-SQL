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

class Customer_p(models.Model):
    customer_id = models.CharField(max_length=10, primary_key=True)
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

    def __str__(self):
        return self.company_name
    
    class Meta:
        db_table = 'customers'	

class Shipper(models.Model):
    shipper_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    phone = models.IntegerField(max_length=24)

    def __str__(self):
        return self.company_name  

    class Meta:
        db_table = 'Shipper'         


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer_p, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField(null=True, blank=True)
    required_date = models.DateField(null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    ship_via = models.ForeignKey(Shipper, on_delete=models.CASCADE,db_column='ship_via')
    freight = models.FloatField(null=True, blank=True)
    ship_name = models.CharField(max_length=40, null=True, blank=True)
    ship_address = models.CharField(max_length=60, null=True, blank=True)
    ship_city = models.CharField(max_length=15, null=True, blank=True)
    ship_region = models.CharField(max_length=15, null=True, blank=True)
    ship_postal_code = models.CharField(max_length=10, null=True, blank=True)
    ship_country = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_id}"
    class Meta:
        db_table = 'orders'


class OrderDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    def __str__(self):
        return f"OrderDetails {self.order}"

    class Meta:
        db_table='order_details'
    
 

