from django import forms
from admn import models
from tinymce.widgets import TinyMCE #tinymce rich text

class productForm(forms.ModelForm):
	# desc = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))
	class Meta:
		model=models.product
		fields=["productCategory", "name", "price", "desc", "img"]
		# widgets = {
  #           'desc': forms.CharField(widget=TinyMCE()),
  #       }

class categoryForm(forms.ModelForm):
	class Meta:
		model=models.product_category
		fields = ['categoryName']