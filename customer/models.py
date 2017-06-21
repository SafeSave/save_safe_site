# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

#upload path
def profile_photo_path(instance, filename):
    return 'customer_{0}/profile/{1}'.format(instance.customer, filename)
# Create your models here.
FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
YEAR_IN_SCHOOL_CHOICES = (
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
)
class Customer(models.Model):
    user = models.OneToOneField(User)
    year = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES,default = FRESHMAN)
    major = models.CharField(max_length = 255, default = 'unkown')
    email = models.EmailField(default='unknown')
    venmo = models.TextField(default = 'unkown') #tempeorarily hold for payment method
    tel = models.TextField(default='unknown')
    address = models.TextField(blank=True)
    zipcode = models.TextField(default=0)
    register_time = models.DateField(default=datetime.date.today)
    is_buyer = models.BooleanField(default = True)
    is_seller = models.BooleanField(default = False)
    buyer_rating = models.DecimalField(default = 0.0)
    seller_rating = models.DecimalField(default = 0.0)
    photo = models.ImageField(upload_to = profile_photo_path, null = True)

    class Meta:
        db_table = 'auth_customer'

    def get_name(self):
        name = self.user.first_name + ' ' + self.user.last_name
        if name is not ' ':
            return name
        return self.user.username

    def set_attributes(self, tel, address, zipcode):
        self.tel = tel if len(tel) < 1 else 'unknown'
        self.address = address if len(address) < 1 else 'unknown'
        self.zipcode = zipcode if len(zipcode) < 1 else 'unknown'

    def calculate_rating(self):
        return 0.0 # function needed to calculate ratings