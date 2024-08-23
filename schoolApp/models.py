from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, datetime


# Create your models here.
#Sitter model
class Sitter(models.Model):
    name = models.CharField(help_text='Write the both first and last name of the sitter', max_length=100)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField(('birth date'), default=date.today)
    gender = models.CharField(max_length=10)
    nin_no = models.CharField(max_length=20, unique=True, blank=True)
    religion = models.CharField(max_length=50, blank=True, default='Christian')
    education_level = models.CharField(max_length=100, blank=True)
    sitter_number = models.CharField(max_length=20, unique=True, blank=True)
    contact = models.CharField(max_length=15, blank=True, default='+256XXXXXXXXX')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

#Baby model
class Baby(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    location = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)    
    baby_number = models.IntegerField()    
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)   
    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    Baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    brought_by = models.CharField(max_length=50)
    period_of_stay = models.CharField(max_length=10)
    fee_amount = models.IntegerField()
    date = models.DateField(default=timezone.now)    
    def __str__(self):
        return self.name

#Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

#Transaction model
class Transaction(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Baby = models.ForeignKey(Baby, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    kind = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.quantity}x {self.Product.name} for purchase #{self.Purchase.id}"