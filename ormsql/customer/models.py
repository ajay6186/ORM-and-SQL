from django.db import models
from store.models import Store
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, null=True, blank=True)
    # address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    activebool = models.BooleanField(default=True)
    create_date = models.DateField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    active = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    