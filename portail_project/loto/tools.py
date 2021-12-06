from django.views.decorators.csrf import csrf_exempt
from django.http import *
from .models import LotoTirage,EuromillionTirage
from bs4 import BeautifulSoup
import requests,random, unicodedata

#urls pour récupérer les données

url_loto="http://loto.akroweb.fr/loto-historique-tirages/"
url_euromillion="http://www.tirage-euromillions.net/euromillions/annees/annee-"

#Fonction pour le loto

def LotoextractTirage(url):
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

def EuromillionExtractTirage(url):
	array=[]
	year=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
	for y in year:
		link=url+str(y)+"/"
		get=requests.get(url)
		html=get.text
		#Lecture de la page html
		#parsing
		HTML = BeautifulSoup(html,'html.parser')
		for tr in HTML.find_all('tr'):
			ligne=[]
			for td in tr.find_all('td'):
				lentd=len(td.text)
				if lentd > 2 :
					ligne.append(td.text.split()[1])
				else:
					ligne.append(td.text)
			if len(ligne) > 1 :
				del ligne[8:10] #j'enleve les gain car osef
				array.append(ligne)
	return array


@csrf_exempt
def BddUpdate(action):
	if action == "loto_bdd_update":
		try:
			tirage_list=LotoextractTirage(url_loto)
			for tirage in tirage_list:
				date=tirage[0]
				numeros=tirage[1:]
				#Verification si la donnée est déjà en base en fonction
				# de la date
				all_tirage=LotoTirage.objects.filter(tl_jour=date)
				if all_tirage.exists():
					print ("deja dans la base")
				else:
					loto_save=LotoTirage(tl_jour=date,tl_tirage=numeros)
					loto_save.save()
			status="[Success] Données ajoutées en base"
			return status
		except:
			status="[Error] Erreur lors de la mise à jour"
			return status
	elif action == "euromillion_bdd_update":
		try:
			tirage_list=EuromillionExtractTirage(url_euromillion)
			print("je suis dans euromillion")
			for tirage in tirage_list:
				date=tirage[0]
				numeros=tirage[1:6]
				numeros_comp=tirage[6:9]
				all_tirage=EuromillionTirage.objects.filter(te_jour=date)
				if all_tirage.exists():
					print ("déjà dans la base")
				else:
					euromillion_save=EuromillionTirage(te_jour=date,te_numeros=numeros,te_numeros_comp=numeros_comp)
					euromillion_save.save()
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
	all_tirage=LotoTirage.objects.values('tl_tirage')
	for tirage in all_tirage:
		a=tirage['tl_tirage'].replace('[','').replace(']','').replace(',','').replace("'","")
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
		all_tirage=LotoTirage.objects.values('tl_jour','tl_tirage')
		tirages={}
		for tirage in all_tirage:
			tirages[tirage['tl_jour']]=tirage['tl_tirage'].replace('[','').replace(']','').replace(',','').replace("'","")
		return tirages
