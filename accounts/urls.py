from django.urls import path
from . import views

urlpatterns = [
	path('', views.home,name='home'),
	path('Client/',views.client,name='client'),
	path('Liste-de-client/',views.list_client,name='liste_client'),
	path('Produit/',views.produit,name='produit'),
	path('ajouter_produits/',views.liste_produit,name='ajout_produit'),
	path('Commande/',views.commande,name='commande'),
	path('ajouter_commande/',views.liste_commande,name='ajout_commande'),
]