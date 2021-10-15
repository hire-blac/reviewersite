from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews', views.reviews, name='reviews'),
    path('reviews/new', views.new_review, name='new_review'),
]
