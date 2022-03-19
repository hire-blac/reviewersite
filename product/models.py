from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
import eav


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.category_name
    
    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category', verbose_name='Select a Category')
    name = models.CharField(max_length=200, verbose_name='Name/Title')
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(default="card-image.svg", null=True, blank=True)

    def __str__(self):
        return self.name
    
    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})


eav.register(Product)