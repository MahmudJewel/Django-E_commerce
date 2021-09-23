from django import forms
from admn import models

class productForm(forms.ModelForm):
	class Meta:
		model=models.product
		fields=["name", "price", "desc", "img"]