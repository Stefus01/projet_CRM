from django.contrib import admin
from .models import Client,Venue,Produit,Commande

# Register your models here.

admin.site.register(Venue)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Commande)