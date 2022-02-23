from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('finduser', views.find_user, name='find_user'),
    # path('products/', views.products, name='products'),
    # path('products/<int:id>', views.products_details, name='products_details'),
    # path('products/new', views.new_product, name='new_product'),

]