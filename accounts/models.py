from django.db import models

# Create your models here.

class Venue(models.Model):
    name=models.CharField('Venue Name',max_length=30)
    address=models.CharField('Venue Address',max_length=300)
    phone=models.CharField(max_length=14)

    def __str__(self):  #allow us to pop up on the page
        return self.name

class Client(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    id_client=models.CharField('Id Client',max_length=3)
    age=models.CharField(max_length=3)
    email=models.EmailField('Email Address',max_length=50)
    address=models.CharField(max_length=300)
    phone=models.CharField('Contact Phone',max_length=14)    

    def __str__(self):  #allow us to pop up on the page
        return self.first_name + ' ' + self.last_name # put first and last name on website

class Produit(models.Model):
    name=models.CharField('Nom du produit',max_length=200)
    type=models.CharField('Type de produit',max_length=200)
    quantity=models.CharField('Quantité',max_length=4)
    price=models.CharField('Prix',max_length=7)

    def __str__(self):  #allow us to pop up on the page
        return self.name