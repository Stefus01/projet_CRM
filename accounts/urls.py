from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.home,name='home'),
	path('client_template/',views.client,name='client'),
	path('liste_de_client/',views.list_client,name='liste_client'),
	path('produit_template/',views.produit,name='produit'),
	path('commande/',views.commande,name='commande'),
]