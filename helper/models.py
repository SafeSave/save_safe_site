# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from customer.models import Customer
import datetime
# Create your models here.
#Payment Choice
THRU_WEBSITE = 'thru_website'
PRIVATE = 'private'
PAYMENT_CHOICES = (
    ('Through website to receive guarantee',THRU_WEBSITE),
    ('Privately',PRIVATE)
)
#Shipping Choice
PICK_UP = 'pick_up'
SHIP = 'ship'
SHIPPING_CHOICES = (
    ('pick up yourself', PICK_UP),
    ('Shipped by seller',SHIP)
)

class Order(models.Model):
    buyer = models.ForeignKey(Customer,on_delete= models.CASCADE, null = True)
    seller = models.ForeignKey(Customer, on_delete= models.CASCADE, null= True)
    order_date = models.DateField(default = datetime.date.today())
    payment_method = models.CharField(max_length= 255, choices= PAYMENT_CHOICES)
    shipping_method = models.CharField(max_length= 255, choices = SHIPPING_CHOICES)

    class Meta:
        db_table = 'order'

def product_photo_path(instance, filename):
    return 'product_{0}/photos/{1}'.format(instance.product.id, filename)


YEAR_CHOICES = ()
for r in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES+=((r, r))

NEW = 'new'
USED = 'used'
CONDITION_CHOICES = (
    ('new', NEW),
    ('used', USED)
) # more choices needed here

class Product(models.Model):
    seller = models.ForeignKey(Customer,on_delete=models.CASCADE, null =True)
    post_date = models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField(upload_to = product_photo_path, null = True)
    official_image = models.ImageField(upload_to = product_photo_path, null = True)
    brand = models.CharField(max_length= 255, default = 'unkown')
    name = models.CharField(max_length = 255, default = 'unkown')
    year_of_purchase = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    condition = models.CharField(max_length = 255, choices = CONDITION_CHOICES, default = NEW)
    location = models.CharField(max_length= 255, null = True) #location package needed to support map display
    available_time = models.DateField(default = datetime.date.today())
    inspection = models.BooleanField(default = True)
    category = models.CharField(max_length= 255, default = 'unkown') # category choices needed

    class Meta:
        db_table = 'product'


class Rating(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null = True)
    rating = models.IntegerField(default = 0)
    comment = models.CharField(null = True)

    class Meta:
        db_table = 'rating'