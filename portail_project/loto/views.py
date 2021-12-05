from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import *
from .tools import *

@csrf_exempt
def home(request):
    post=request.POST.get('x')
    y=BddUpdate(post)
    return render(request,'loto/index.html',{'status':y})

def Simulation(request):
    post=request.POST.get('x')
    if (post.isnumeric() == True):
        res=TirageSimulation(post)
    else:
        print("Erreur")
    return render(request,'loto/simulation.html',{'tirages':res})

def LotoDatatable(request):
    x=request.POST.get('id')
    tirage=DisplayLotoData(x)
    return JsonResponse(tirage)