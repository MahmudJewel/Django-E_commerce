from django import template
# from django.contrib.sessions import session

register = template.Library()

@register.filter(name='in_cart')
def in_cart(product, cart_item):
	for i in cart_item:
		if int(i)==product.id:
			return True
	return False

@register.filter(name='product_amount')
def product_amount(request, id):
	id=str(id)
	cart=request.session.get('cart')
	return cart[id]


@register.filter(name='single_product_price')
def single_product_price(price, id):
	#cart=session.get('cart')
	# amount=cart[id]
	return price*id