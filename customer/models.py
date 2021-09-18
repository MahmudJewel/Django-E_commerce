from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    birth_date = models.DateField(default=datetime.now)
    profile_pic= models.ImageField(default='profile_pic/customer.png', upload_to='profile_pic/Customer/', null=True, blank=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)

    def save(self):    #resize image
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = ( 300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver (signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('Customer is created')
        Customer.objects.create(user=instance) #Customer objects will be created
    else:
        print('Not created')

'''
@receiver (signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print('Customer is saved')
    instance.profile.save()
'''