from django.db import models
# django rich text  
from tinymce import models as tinymce_models 

# Create your models here.

class product_category(models.Model):
	categoryName=models.CharField(max_length=20)

	def __str__(self):
		return self.categoryName


class product(models.Model):
	productCategory=models.ForeignKey(product_category, on_delete=models.SET_NULL, null=True, blank=True )
	name =models.CharField(max_length=50)
	price = models.PositiveIntegerField()
	desc =tinymce_models.HTMLField(null=True,blank=True)
	img =models.ImageField(default="product/default.png", upload_to="product/", null=True, blank=True)

	def __str__(self):
		return self.name

