from django import forms
from django.forms import ModelForm
from .models import Venue,Client,Produit

#Create a Venue form
class VenueForm(ModelForm):
    class Meta: #define things in clasx for django
        model=Venue
        fields =('name','phone','address',)
        
class ClientForm(ModelForm):
    class Meta: #define things in clasx for django
        model=Client
        fields =('first_name','last_name','age','address','email','phone')

class ProduitForm(ModelForm):
    class Meta: #define things in clasx for django
        model=Produit
        fields =('__all__')
        