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

# Car Attributes
# Attribute.objects.create(name='make', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='model', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='year', datatype=Attribute.TYPE_TEXT)

# Book Attributes
# Attribute.objects.create(name='author', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='summary', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='ISBN', datatype=Attribute.TYPE_TEXT)

# Music Attributes
# Attribute.objects.create(name='artist', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='featuring', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='album', datatype=Attribute.TYPE_TEXT)
# Attribute.objects.create(name='year', datatype=Attribute.TYPE_TEXT)

eav.register(Product)