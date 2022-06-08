from django.shortcuts import render
from .forms import VenueForm
# from .forms import Client

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def client(request):
	return render(request,'client_template.html')

def VenueForm(request):
	return render(request,'add_venue.html')