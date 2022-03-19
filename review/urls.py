from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug1>/<slug:slug>', views.review, name='review_details'),
    path('new', views.new_review, name='new_review'),
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote'),
    path('comment', views.new_comment, name='new_comment'),
]