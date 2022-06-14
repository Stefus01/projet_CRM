from multiprocessing import Event
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Client,Produit,Commande
from .forms import ClientForm, CommandeForm, ProduitForm, VenueForm

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def commande(request): #pour remplire commande
	cr_commande=Commande.objects.all()
	context={'liste_commandes':cr_commande}
	return render(request, 'Commande.html', context)

def liste_commande(request):
	submitted=False
	if request.method == "POST":
		form= CommandeForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ajouter_commande?submitted=True')
	else:
		form= CommandeForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'ajouter_commande.html',{'form':form, 'submitted':submitted})

def produit(request): #pour remplire produit
	all_fields = Produit.objects.all()
	context = {'champs_liste' : all_fields}
	return render(request, 'Produit.html', context)

def liste_produit(request):
	submitted=False
	if request.method == "POST":
		form= ProduitForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ajouter_produits?submitted=True')
	else:
		form= ProduitForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'ajouter_produits.html',{'form':form, 'submitted':submitted})

def list_client(request): # pour afficher liste client
	client_list=Client.objects.all() #put all the client object of cleint 
	return render(request,'Liste-de-client.html',{'client_list': client_list})

def client(request): #pour remplire formulaire client
	submitted=False
	if request.method == "POST":
		form= ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Client/?submitted=True')
	else:
		form= ClientForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'Client.html',{'form':form, 'submitted':submitted})

def add_venue(request): #test/ example
	submitted=False
	if request.method == "POST":
		form= VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	else:
		form= VenueForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'add_venue.html',{'form':form, 'submitted':submitted})