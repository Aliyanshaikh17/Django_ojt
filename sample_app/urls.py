from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home , name='home'),
   path('post_data/' , views.post_data , name='post_data'),
   path('get_all_data/', views.get_all_data , name='get_all_data'),
   path('get/<int:pk>/', views.get_one , name='get_one')
]
