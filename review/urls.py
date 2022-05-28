from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug1>/<slug:slug>', views.review, name='review_details'),
    path('<slug:slug1>/<slug:slug>/edit', views.edit_review, name='edit_review'),
    path('new', views.new_review, name='new_review'),
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote'),
    path('comment', views.new_comment, name='new_comment'),
    path('reply', views.new_reply, name='new_reply'),
]