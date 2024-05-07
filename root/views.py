from django.shortcuts import render

from django.http import HttpResponse

def func_home(request):
    return render(request,'root/index.html')

def func_detail(request):
    return render(request,'root/portfolio-details.html')

# Create your views here.
