from django.http import HttpResponse
from django.shortcuts import render

def home_index(request):
    return render(request,'base/gs_home.html')
