from django.shortcuts import render

from django.http import HttpResponse

def func_home(request):
    return render(request,'root/index.html')

def func_contact(request):
    return render(request,'root/contact.html')


def func_about_us(request):
    return render(request,'root/about.html')


def func_stuff(request):
    return render(request,'root/stuff.html')

# Create your views here.
