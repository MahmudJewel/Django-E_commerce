from django import template
from admn import models as AMODEL

register = template.Library()

#Check the prouct is on cart or not.Base of this, add or remove button set
@register.filter(name='in_cart')
def in_cart(product, cart_item):
	for i in cart_item:
		if int(i)==product.id:
			return True
	return False


#Return the indivisual product number
@register.filter(name='product_amount')
def product_amount(request, id):
	id=str(id)
	cart=request.session.get('cart')
	return cart[id]


#Return the single product's total price
@register.simple_tag
def single_product_price(request, price, pk):
	cart=request.session.get('cart')
	pk=str(pk)
	amount=cart[pk]
	#print(f"amount {type(amount)} {amount}")
	return price*amount


#total price in cart page
@register.simple_tag
def total_price(request):
	cart=request.session.get('cart')
	#print(f"keys {type(cart.keys())}")
	sum=0
	if cart:
		for key in cart.keys():
			product=AMODEL.product.objects.get(id=key)
			sum=sum+single_product_price(request, product.price, key)
		
	return sum
