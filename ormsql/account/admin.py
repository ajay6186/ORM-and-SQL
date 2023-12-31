from django.contrib import admin

# Register your models here.
from .models import User

# class UserAdmin()

admin.site.register(User)