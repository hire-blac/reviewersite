from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('edit', views.edit_profile, name='edit_profile'),
    path('<slug:slug>', views.user_profile, name='user_profile'),
    path('<slug:slug>/follow', views.follow, name='follow'),
    path('<slug:slug>/unfollow', views.unfollow, name='unfollow'),
    path('<slug:slug>/followings', views.followings, name='followings'),
]