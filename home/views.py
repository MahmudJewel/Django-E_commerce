from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from admn import forms as AFORM
from admn import models as AMODEL

from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.

#Adding item on Cart
def add_to_cart(request, id):
	cart = request.session.get('cart')
	if cart:
		cart[id]=1
	else:
		cart={}
		cart[id]=1
	request.session['cart']=cart
	return 0

#Removing from Cart
def remove_from_cart(request, pk):
	pk=str(pk)
	cart = request.session.get('cart')
	cart.pop(pk)
	request.session['cart']=cart
	return 0


#Home page, adding item, removing item from cart
def home(request):
	if request.user.is_authenticated:
		#print(f"User = {request.user} ID = {request.user.id}")
		HttpResponseRedirect('afterlogin')

	products=AMODEL.product.objects.all()
	categories = AMODEL.product_category.objects.all()
	
	if request.method=='POST':
		pdid=request.POST.get('idfromhtml')
		#print(f"type pdid {type(pdid)}")
		if 'addToCart' in request.POST:
			add_to_cart(request, pdid) #Call the function
			'''
			qntt=cart.get(pdid)
			if qntt:
				cart[pdid]=qntt+1
			else:
				cart[pdid]=1 '''
		elif 'rmvFromCart' in request.POST:
			pdid=request.POST.get('idfromhtml')
			remove_from_cart(request, pdid)
	
	context = {
		'products' : products,
		'categories' : categories,
	}
	#print(f"home/cart{request.session['cart']}")
	return render(request, 'home/home.html', context)


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
	if is_customer(request.user):
		messages.success(request, f"Successfully login for {request.user}")
		return redirect('/')

	else:
		return HttpResponseRedirect('admn/dashboard')


#Single product view, Single product details on single page, adding & removing on cart
def product_view(request, pk):
		pd=AMODEL.product.objects.get(id=pk)
		context={
			'pd': pd,
		}
		#print(f'type= {type(pk)}')
		if request.method=='POST':
			if 'addToCart' in request.POST:
				add_to_cart(request, pk)

			elif 'rmvFromCart' in request.POST:
				remove_from_cart(request, pk)
				print(f"type {type(pk)}")
				adr='/#'+str(pk) #return to home page same product
				return redirect(adr)
				# remove_from_cart(request, pk)

		return render(request, 'home/product.html', context)

#Cart page
def cart_view(request):
	cart_item=request.session.get('cart')
	#print(f"cart item {cart_item['4']}")
	products=[]
	if cart_item:
		for keys in cart_item:
			product = AMODEL.product.objects.get(id=keys)
			products.append(product)

	if request.method=='POST':
		tid=request.POST.get('tid')
		qntt=cart_item[tid]
		if 'plus' in request.POST:
			cart_item[tid]=qntt+1

		elif 'minus' in request.POST:
			if(qntt>1):
				cart_item[tid]=qntt-1
			else:
				pass
		
		elif 'rm' in request.POST:
			remove_from_cart(request, tid)
			return redirect('cart')

		request.session['cart']=cart_item
		#print(f"cart {cart_item}")

	#products=AMODEL.product.objects.get(id=6)
	context={
		'products' :  products,
	}
	return render(request, 'home/cart.html', context) 

# checkout page for giving shipping address
def checkout_view(request):
	cart_item=request.session.get('cart')
	#print(f"cart item {cart_item['4']}")
	products=[]
	if cart_item:
		for keys in cart_item:
			product = AMODEL.product.objects.get(id=keys)
			products.append(product)

	# userForm=CFORM.shippingUserPart1(instance = request.user)
	# customerForm=CFORM.shippingUserPart2(instance=request.user.profile)
	user=CMODEL.User.objects.get(id=request.user.id)
	customer=CMODEL.Customer.objects.get(user=user)
	if request.method=='POST':
		fname=request.POST.get('firstName')
		lname=request.POST.get('lastName')
		fullName = fname+" "+lname,
		mobile = request.POST.get('mobile')
		address = request.POST.get('address')
		#print('cart length = ', len(request.session['cart']))

		if(request.session.get('cart')):
			# order placed when cart has at least 1 item
			if(len(request.session['cart']) >=1): #cart item check
				for p in products:
					cart_key=str(p.id)
					order= CMODEL.order(
						product = p,
						customer = user,
						price = p.price,
						qntt = cart_item[cart_key],
						fullName = fullName,
						mobile = mobile,
						address = address)
					order.saveOrder()
				del request.session['cart']
				messages.success(request, f"Your order has been placed Successfully")
				return redirect('/')
			
				
		else:
			messages.success(request, f"Please add item to cart and check out.")
		#print(f'your order {order} ')

	
	context={
		'products': products,
		'user': user,
		'customer' : customer,

	}
	return render(request, 'home/checkout.html', context)
