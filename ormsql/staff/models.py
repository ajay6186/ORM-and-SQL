from django.db import models
from django.utils import timezone
from store.models import Store
from address.models import Address
# Create your models here.
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    email = models.CharField(max_length=50, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40)
    last_update = models.DateTimeField(default=timezone.now)
    picture = models.BinaryField(null=True, blank=True)  # Assuming bytea corresponds to BinaryField

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.first_name} {self.last_name}, Username: {self.username}"
    