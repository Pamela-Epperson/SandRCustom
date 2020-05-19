
from django.db import models
import re



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    c_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(default = 0.00, max_digits=5, decimal_places=2)
    color1 = models.CharField(default ="color", max_length=45)
    color2 = models.CharField(default ="color", max_length=45)
    text = models.CharField(default ="text", max_length=255)
    logo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

# Create your models here.
