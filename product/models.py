from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
import eav
from reviewer.unique import unique_slug_generator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category', verbose_name='Select a Category')
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='products/',default="placeholder-image.jpg", null=True, blank=True)

    def __str__(self):
        return self.name
    
    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})

    
class ProductAttribute(models.Model):
    category = models.ManyToManyField(Category, related_name='attrbCategory')
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    
    def __str__(self):
        return self.name

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name)
        return super().save(*args, **kwargs)

    
class ProductAttribValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Valueproduct')
    productAttribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='attribute')
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.product}: {self.productAttribute} = {self.value}'

# eav.register(Product)
