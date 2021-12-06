from django.views.decorators.csrf import csrf_exempt
from django.http import *
from .models import LotoTirage,EuromillionTirage
from bs4 import BeautifulSoup
import requests,random, unicodedata



url="http://loto.akroweb.fr/loto-historique-tirages/"

def extractTirage(url):
	#initiation array
	array=[]
	#gotot
	#recupération contenu de la page web
	get=requests.get(url)
	html=get.text
	#Parsing
	HTML = BeautifulSoup(html,'html.parser')
	#Extraction des numeros sortis
	for lignes in HTML.find_all('tr'):
		tirage=[]
		for cellules in lignes.find_all('td'):
			values=str(cellules.string)
			numeros=[]
			if values != "None":
				tirage.append(values)
		del tirage[0]
		array.append(tirage)
	return array


@csrf_exempt
def BddUpdate(action):
    if action == "bdd_update":
        try:
            tirage_list=extractTirage(url)
            for tirage in tirage_list:
                date=tirage[0]
                numeros=tirage[1:]
                #Verification si la donnée est déjà en base en fonction
                # de la date
                all_tirage=LotoTirage.objects.filter(t_jour=date)
                if all_tirage.exists():
                    print ("déjà dans la base")
                else:
                    loto_save=LotoTirage(t_jour=date,t_tirage=numeros)
                    loto_save.save()
            status="[Success] Données ajoutées en base"
            return status
        except:
            status="[Error] Erreur lors de la mise à jour"
            return status
def RemoveDuplicates(a):
    b = list()
    for sublist in a:
        if sublist not in b:
            b.append(sublist)
    return b

def TirageSimulation(x):
    #Extraction des tirages
    print(x)
    numbers=[]
    X=[] #array pour les numéros qui sortent le plus souvent
    final=[] #array final
    all_tirage=LotoTirage.objects.values('t_tirage')
    for tirage in all_tirage:
        a=tirage['t_tirage'].replace('[','').replace(']','').replace(',','').replace("'","")
        nb_array=a.split()
        del nb_array[-1]
        for nb in nb_array:
            chiffre=int(nb)
            numbers.append(chiffre)

    numbers_uniq=RemoveDuplicates(numbers)
    total=all_tirage.count()
    for n in numbers_uniq:
        count=int(numbers.count(n))
        countp=float(numbers.count(n))
        percent_tmp=((countp/total)*100)
        percent=round(percent_tmp,2)
		# print ("le % de "+str(n)+" est de "+str(percent))
        if (percent > 10):
            X.append(n)
    i=0
    while i < int(x):
        t=random.sample(X,5)
        final.append(t)
        i+=1
    return final

def DisplayLotoData(x):
	if x == "loto_datatable":
		all_tirage=LotoTirage.objects.values('t_jour','t_tirage')
		tirages={}
		for tirage in all_tirage:
			tirages[tirage['t_jour']]=tirage['t_tirage'].replace('[','').replace(']','').replace(',','').replace("'","")
		return tirages
