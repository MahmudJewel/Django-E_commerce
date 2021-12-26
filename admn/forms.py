from django import forms
from admn import models
from tinymce.widgets import TinyMCE #tinymce rich text
# from tinymce import TinyMCE

# class TinyMCE(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False

class productForm(forms.ModelForm):
	# desc = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))
	class Meta:
		model=models.product
		fields=["productCategory", "name", "price", "desc", "img"]
		# widgets = {'desc' : forms.CharField(
  #       	widget=TinyMCE(
  #           attrs={'required': False, 'cols': 30, 'rows': 10}
  #       				)
  #   		)}

		# widgets = {
  #           'desc': forms.CharField(widget=TinyMCE(attrs={'required': False, 'cols': 30, 'rows': 10})),
  #       }

  		

class categoryForm(forms.ModelForm):
	class Meta:
		model=models.product_category
		fields = ['categoryName']