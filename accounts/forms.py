from django import forms
from django.forms import ModelForm
from .models import Venue,Client,Produit,Commande

#Create a Venue form
class VenueForm(ModelForm):
    class Meta: #define things in class for django
        model=Venue
        fields =('name','phone','address',)
        
class ClientForm(ModelForm):
    class Meta: #define things in class for django
        model=Client
        fields =('first_name','last_name','age','address','email','phone')

class ProduitForm(ModelForm):
    class Meta: #define things in class for django
        model=Produit
        fields =('__all__')
        
class CommandeForm(ModelForm):
    class Meta: #define things in class for django
        model = Commande
        fields = ('num_order', 'num_cli', 'name_cli', 'total')
