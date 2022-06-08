from django.contrib import admin
from .models import Client
from .models import Produit
from .models import Venue

# Register your models here.

admin.site.register(Venue)
admin.site.register(Client)
admin.site.register(Produit)
