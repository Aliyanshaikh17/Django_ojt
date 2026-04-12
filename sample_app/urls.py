from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home , name='home'),
   path('post_data/' , views.post_data , name='post_data')
]
