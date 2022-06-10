from multiprocessing import Event
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Client,Produit
from .forms import ClientForm, VenueForm

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def produit(request):
	all_fields = Produit.objects.all()
	context = {'champs_liste' : all_fields}
	return render(request, 'produit_template.html', context)

def list_client(request): # pour afficher liste client
	client_list=Client.objects.all() #put all the client object of cleint 
	return render(request,'liste_de_client.html',{'client_list': client_list})

def client(request): #pour remplire formulaire client
	submitted=False
	if request.method == "POST":
		form= ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/client_template/?submitted=True')
	else:
		form= ClientForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'client_template.html',{'form':form, 'submitted':submitted})

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