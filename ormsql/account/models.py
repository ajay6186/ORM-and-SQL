from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255, blank = True, null = True)
    email = models.CharField(max_length=255)
    password = models.DateTimeField(auto_now_add=True)
    email_verify = models.BooleanField()

    def __str__(self):
        return self.name