from django.contrib import admin
from django.urls import path
from .views import * 


urlpatterns = [
    path('',func_home),
    path('contact/',func_contact),
    path('about_us/',func_about_us),
    path('stuff/',func_stuff),
]
