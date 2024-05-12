from django.shortcuts import render
from django.http import JsonResponse
from .ChessBind import driver

def index(request):
    return JsonResponse({'foo': 'bar'})

def posmove(request):
    return JsonResponse(driver.allmoves())

def play(request):
    return JsonResponse(driver.allmoves())
# Create your views here.
