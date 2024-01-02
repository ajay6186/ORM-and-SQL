from django.db import models
# from staff.models import Staff
from django.utils import timezone
from address.models import Address

# Create your models here.
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey('self', on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'store'

    def __str__(self):
        return f"Store ID: {self.store_id}, Manager: {self.manager_staff}, Address: {self.address}"
    
