from django.shortcuts import render
from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.

def home(request):
	return render(request,'home/home.html')
