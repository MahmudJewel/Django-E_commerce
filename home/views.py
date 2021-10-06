from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from admn import forms as AFORM
from admn import models as AMODEL

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		HttpResponseRedirect('afterlogin')
	products=AMODEL.product.objects.all()
	context = {
		'products' : products,
	}
	return render(request, 'home/home.html', context)

'''
def customer_home(request):
	return render(request,'home/home.html')
	'''

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
	if is_customer(request.user):
		messages.success(request, f"Successfully login for {request.user}")
		return redirect('/')

	else:
		return HttpResponseRedirect('admn/dashboard')

def product_view(request, pk):
		pd=AMODEL.product.objects.get(id=pk)
		context={
			'pd': pd,
		}
		return render(request, 'home/product.html', context)

def cart_view(request):
	products=AMODEL.product.objects.get(id=6)
	context={
		't' :  products,
	}
	return render(request, 'home/cart.html', context)

