from django.db import models

#For including phone number field in djangoproject
from phone_field import PhoneField

# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=50, help_text='Your GoodName')
    Email = models.EmailField(max_length=254, blank=True, help_text='abc@gmail.com')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    Address = models.CharField(max_length=524, help_text='Your Address')
