from django.contrib import admin
from customer import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.order)
