from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('finduser', views.find_user, name='find_user'),
]