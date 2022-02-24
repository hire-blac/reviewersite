from unicodedata import category
from django.db import models
import eav
from eav.models import Attribute


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


eav.register(Product)