from django.shortcuts import render
from django.http import JsonResponse
from .ChessBind import driver

def index(request):
    return render(request,'brainwork/home.html',{'title':'home-page'})

def posmove(request):
    if request.method == 'POST':
        return JsonResponse(driver.allmoves(request.POST['value']))
    return render(request,'brainwork/value.html',{'title':'value-page','input':'POSMOVE'})

def play(request):
    if request.method == 'POST':
        return JsonResponse(driver.play(request.POST['value']))
    return render(request,'brainwork/value.html',{'title':'value-page','input':'PLAY'})
# Create your views here.
