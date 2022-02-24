from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_product, name='new_product'),
    path('<int:id>', views.product, name='product'),
    path('', views.product_search, name='products_search'),
]