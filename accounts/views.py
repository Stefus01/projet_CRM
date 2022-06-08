from django.shortcuts import render
# from .forms import Client

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def client(request):
	return render(request,'client_template.html')
