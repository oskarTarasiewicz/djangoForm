from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', views.users, name='users'),
    path('delete/', views.delete, name='delete'),
    path('delete_player/', views.delete_player, name='delete_player'),
    path('insert_player/', views.insert_player, name='insert_player'),
]
