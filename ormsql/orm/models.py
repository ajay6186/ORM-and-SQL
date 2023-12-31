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
