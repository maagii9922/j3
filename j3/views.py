from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch

def index(request):
    return HttpResponse('welcome')

def home(request):
    return render(request,'index.html')

def m(request):
    data=Hereglegch.objects.all()
    return render(request,'index.html',{'ddd':data})