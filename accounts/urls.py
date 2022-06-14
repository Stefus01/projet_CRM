from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.home,name='home'),
	path('Client/',views.client,name='client'),
	path('Liste-de-client/',views.list_client,name='liste_client'),
	path('Produit/',views.produit,name='produit'),
	path('Commande/',views.commande,name='commande'),
]