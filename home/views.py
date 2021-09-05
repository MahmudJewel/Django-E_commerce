from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		HttpResponseRedirect('home')
	return render(request,'home/home.html')
