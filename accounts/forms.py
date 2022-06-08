from django import forms
from django.forms import ModelForm
from .models import Venue

#Create a Venue form
class VenueForm(ModelForm):
    class Meta: #define things in clasx for django
        model=Venue
        fields =('name','phone','address',)
        