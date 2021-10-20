from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/<int:id>', views.review, name='review'),
    path('reviews', views.reviews, name='reviews'),
    path('myreviews', views.my_reviews, name='myreviews'),
    path('reviews/new', views.new_review, name='new_review'),
]
