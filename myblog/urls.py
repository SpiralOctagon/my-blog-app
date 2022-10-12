from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('', views.home, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('login/', views.login, name='login'),
]
