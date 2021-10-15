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

	if request.method=='POST':
		pdid=request.POST.get('idfromhtml')
		print(f"type of pdid={type(pdid)}")
		#product=AMODEL.product.objects.get(id=pdid)
		#print('product: ', product.price)
		#print('product id= ', pdid)
		cart = request.session.get('cart')
		if cart:
			qntt=cart.get(pdid)
			if qntt:
				cart[pdid]=qntt+1
			else:
				cart[pdid]=1
		else:
			cart={}
			cart[pdid]=1
		request.session['cart']=cart
		print('cart' , request.session['cart'])

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
		#print(f'type= {type(pk)}')
		if request.method=='POST':
			cart = request.session.get('cart')
			if cart:
				pk=str(pk)
				qntt=cart.get(pk)
				if qntt:
					cart[pk]=qntt+1
				else:
					cart[pk]=1
			else:
				cart={}
				cart[pk]=1
			request.session['cart']=cart
			print(f"pk={pk} + cart= {cart}")
		return render(request, 'home/product.html', context)

def cart_view(request):
	cart_item=request.session.get('cart')
	products=[]
	if cart_item:
		for keys in cart_item:
			product = AMODEL.product.objects.get(id=keys)
			products.append(product)
	#products=AMODEL.product.objects.get(id=6)
	context={
		'products' :  products,
	}
	return render(request, 'home/cart.html', context) 

