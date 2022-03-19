from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_product, name='new_product'),
    path('<slug:slug>', views.product, name='product_details'),
    path('', views.product_search, name='products_search'),
]