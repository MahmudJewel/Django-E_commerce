from django.db import models

# Create your models here.

class product(models.Model):
	name =models.CharField(max_length=50)
	price = models.PositiveIntegerField()
	desc =models.CharField(max_length=60)
	img =models.ImageField(default="product/default.png", upload_to="product/", null=True, blank=True)

	def __str__(self):
		return self.name