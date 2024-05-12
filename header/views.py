from django.shortcuts import render
from django.http import JsonResponse
from . import driver

def index(request):
    return JsonResponse({'foo': 'bar'})

def player(request):
    return JsonResponse(driver.allmoves())
# Create your views here.
