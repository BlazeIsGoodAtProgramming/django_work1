from django.contrib import admin
from django.urls import path
from .views import * 

app_name ='root'

urlpatterns = [
    path('',func_home , name = 'home'),
    path('detail/',func_detail , name = 'detail' ),
]
