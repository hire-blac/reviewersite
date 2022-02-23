from django.contrib import admin
from . models import *
from . forms import ProductAdminForm
from eav.admin import BaseEntityAdmin


class ProductAdmin(BaseEntityAdmin):
    form = ProductAdminForm


# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)