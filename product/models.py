import imp
from django.urls import reverse
from django.db import models
import eav
from eav.models import Attribute


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category', verbose_name='Select a Category')
    name = models.CharField(max_length=200, verbose_name='Name/Title')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'id': self.pk})


eav.register(Product)