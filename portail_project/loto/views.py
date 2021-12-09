from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import *
from .tools import *

@csrf_exempt
def home(request):
    return render(request,'loto/index.html')

def LotoUpdate(request):
    post=request.POST.get('x')
    y=BddUpdate(post)
    return render(request,'loto/loto_update.html',{'status':y})

def EuromillionBdd(request):
    post=request.POST.get('x')
    y=BddUpdate(post)
    return render(request,'loto/euromillion_update.html',{'status':y})


def Simulation(request):
    post=request.POST.get('x')
    if (post.isnumeric() == True):
        res=TirageSimulation(post)
    else:
        print("Erreur")
    return render(request,'loto/loto_simulation.html',{'tirages':res})

def LotoDatatable(request):
    x=request.POST.get('id')
    tirage=DisplayLotoData(x)
    return JsonResponse(tirage)
