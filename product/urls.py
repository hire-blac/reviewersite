from django.urls import path
from . import views

urlpatterns = [
    
    path('new', views.new_product, name='new_product'),
    path('<int:id>', views.product, name='product'),
    # path('finduser', views.find_user, name='find_user'),
    path('', views.product_search, name='products_search'),
    # path('products/<int:id>', views.products_details, name='products_details'),
    # path('products/new', views.new_product, name='new_product'),

]