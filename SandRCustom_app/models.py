from __future__ import unicode_literals
from django.db import models
import re
import datetime


# class ProductManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['product']) ==0:
#             errors['name'] = "A product must be provided"
#         if len(postData['product']) < 3:
#             errors['name'] = "Product must be at least 3 characters"
#         if len(postData['description']) == 0:
#             errors['name'] = "A description must be provided"
#         if len(postData['description']) < 3:
#             errors['name'] = "Description should be at least 15 characters"            
#         return errors

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
    date_added = models.DateField(default=datetime.date.today)
    poster = models.ForeignKey(User, related_name='user_products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ProductManager()

# Create your models here.
