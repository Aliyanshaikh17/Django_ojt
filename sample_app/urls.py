from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home , name='home'),
   path('post_data/' , views.post_data , name='post_data'),
   path('get_all_data/', views.get_all_data , name='get_all_data'),
   path('get/<int:pk>/', views.get_one , name='get_one'),
   path('put/<int:pk>/', views.put_stu , name='put'),
   path('delete/<int:pk>/', views.delete_stu , name='delete_stu'),
   path('register/', views.register , name='register'),
   path('login/', views.login , name='login')
]
