from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from customer.models import Customer

'''
@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		print('Customer is created')
		Customer.objects.create(user=instance) #Customer objects will be created

@receiver (post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	print('Customer is saved')
	instance.profile.save() #profile is the OneToOneField name. see the customer model
'''