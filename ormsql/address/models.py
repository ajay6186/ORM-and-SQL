from django.db import models
from django.utils import timezone

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.country
    
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return f"Address ID: {self.address_id}, City: {self.city}, District: {self.district}, Postal Code: {self.postal_code}"