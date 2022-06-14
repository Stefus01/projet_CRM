from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signin(request):
    return render(request, 'Signin.html')

def signout(request):
    pass

def signup(request):
    if request.method=="POST":
        username=request.POST['UserName']
        fname=request.POST['FName']
        lname=request.POST['LName']
        email=request.POST['Email']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm_Password']

        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, " Your account has been succesfully created.")
        # return HttpResponseRedirect('/signup/?submitted=True')

    return render(request, 'Signup.html')