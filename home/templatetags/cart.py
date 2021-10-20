from django import template

register = template.Library()

@register.filter(name='in_cart')
def in_cart(product, cart_item):
	for i in cart_item:
		if int(i)==product.id:
			return True
	return False