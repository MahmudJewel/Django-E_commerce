from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('afterlogin')
	return render(request,'home/home.html')

def customer_home(request):
	return render(request,'home/home.html')
	
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
	if is_customer(request.user):
		return redirect('home/')

	else:
		return HttpResponseRedirect('admn/dashboard')

