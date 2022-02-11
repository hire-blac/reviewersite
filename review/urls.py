from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.review, name='review'),
    path('new', views.new_review, name='new_review'),
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote'),

]