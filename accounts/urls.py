from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('edit', views.edit_profile, name='edit_profile'),
    path('<int:id>', views.user_profile, name='user_profile'),
    path('<int:id>/follow', views.follow, name='follow'),
    path('<int:id>/unfollow', views.unfollow, name='unfollow'),
]