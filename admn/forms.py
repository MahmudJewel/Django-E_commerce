from django import forms
from admn import models

class productForm(forms.ModelForm):
	class Meta:
		model=models.product
		fields=["name", "price", "desc", "img"]

class categoryForm(forms.ModelForm):
	class Meta:
		model=models.product_category
		fields = ['categoryName']