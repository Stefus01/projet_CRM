from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import VenueForm
# from .forms import Client

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def client(request):
	return render(request,'client_template.html')

def add_venue(request):
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