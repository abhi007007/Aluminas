from django import views
from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),

]