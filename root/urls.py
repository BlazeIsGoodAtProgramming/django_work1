from django.contrib import admin
from django.urls import path
from .views import * 


urlpatterns = [
    path('',func_home),
    path('detail/',func_detail),
]
