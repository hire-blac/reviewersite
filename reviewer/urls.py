from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('reviews', views.reviews, name='reviews'),
    path('reviews/<int:id>', views.review, name='review'),
    path('reviews/new', views.new_review, name='new_review'),
    path('finduser', views.find_user, name='find_user'),
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote'),
    path('products/', views.products, name='products'),
    path('products/<int:id>', views.products_details, name='products_details'),
    path('products/new', views.new_product, name='new_product'),

]