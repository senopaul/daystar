CodeCHecks

<select
            aria-hidden="true"
            tabindex="-1"
            style="position: absolute; border: 0px; width: 1px; height: 1px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; overflow-wrap: normal;"
          >
<option value=""></option>
<option value="Female">{{sitter.gender}}</option>
<option value="Male">{{sitter.gender}}</option>
</select>

<select
            aria-hidden="true"
            tabindex="-1"
            style="position: absolute; border: 0px; width: 1px; height: 1px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; overflow-wrap: normal;"
          >
<option value=""></option>
{% for sitter in sitters %}
<option value="{{sitter.id}}">{{sitter.gender}}</option>

            {% endfor %}


</select>

<div class="rounded-lg bg-card text-card-foreground shadow-sm border-2 border-green-500 flex flex-col items-center justify-center p-8" data-v0-t="card">
        <div class="p-6 flex flex-col items-center justify-center">
          <h2 class="text-2xl font-bold mb-2 text-green-500">Baby Attendance</h2>
          <p class="text-gray-500 mb-4 text-center">
            Monitor the attendance of all babies enrolled in the daycare.
          </p>
          <button class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 px-4 py-2 bg-green-500 hover:bg-green-600 text-white">
            View Report
          </button>
        </div>
      </div>

      <button class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white">
            View Report
          </button>

class Baby(models.Model):
name = models.CharField(max_length=255)
gender = models.CharField(max_choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
age = models.PositiveIntegerField()
location = models.CharField(max_length=255)
brought_by = models.CharField(max_length=255) # Name of the person who brought the baby
arrival_time = models.DateTimeField(auto_now_add=True) # Automatically record arrival time
parents_names = models.CharField(max_length=255)
fee_amount = models.DecimalField(max_digits=10, decimal_places=2) # Fee in Ugandan Shillings
period_of_stay = models.CharField(max_length=255) # Options like half-day, full-day, monthly
baby_number = models.CharField(max_length=20, unique=True) # Unique identifier for the baby  
 def **str**(self):
return self.name

#Sitter model
class Sitter(models.Model):
name = models.CharField(max_length=255)
location = models.CharField(max_length=255)
date_of_birth = models.DateField()
gender = models.CharField(max_choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
next_of_kin_name = models.CharField(max_length=255)
nin_no = models.CharField(max_length=20, unique=True) # National Identification Number (unique)
recommender_name = models.CharField(max_length=255, blank=True)
religion = models.CharField(max_length=255, blank=True)
education_level = models.CharField(max_length=255)
sitter_number = models.CharField(max_length=20, unique=True) # Unique identifier for the sitter
contact_number = models.CharField(max_length=20)
is_active = models.BooleanField(default=True) # Flag to mark if sitter is currently employed

def **str**(self):
return self.name

class Product(models.Model):
name = models.CharField(max_length=255)
description = models.TextField(blank=True)
unit_price = models.DecimalField(max_digits=10, decimal_places=2)
unit = models.CharField(max_length=50, blank=True) # Optional unit (e.g., dozen, kg)
is_doll = models.BooleanField(default=False) # Flag to indicate if it's a doll

    def __str__(self):
        return self.name

class Stock(models.Model):
product = models.ForeignKey(Product, on_delete=models.CASCADE)
quantity = models.PositiveIntegerField()
def **str**(self):
return f"{self.product.name} (Stock: {self.quantity})"

class Purchase(models.Model):
vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # Link to Vendor model
purchase_date = models.DateField(auto_now_add=True)
total_amount = models.DecimalField(max_digits=10, decimal_places=2)
def **str**(self):
return f"Purchase from {self.vendor.name} on {self.purchase_date}"

class PurchaseItem(models.Model):
purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
product = models.ForeignKey(Product, on_delete=models.CASCADE)
quantity = models.PositiveIntegerField()
unit_price = models.DecimalField(max_digits=10, decimal_places=2)
total_price = models.DecimalField(max_digits=10, decimal_places=2)
def **str**(self):
return f"{self.quantity}x {self.product.name} for purchase #{self.purchase.id}"

class Vendor(models.Model):
name = models.CharField(max_length=255)
contact_number = models.CharField(max_length=20, blank=True)
address = models.TextField(blank=True)

    def __str__(self):
        return self.name

........................

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

# Create your models here.

#Baby model
class Baby(models.Model):
name = models.CharField(max_length=100)
gender = models.CharField(max_length=10)
dob = models.DateField(('birth date'))
location = models.CharField(max_length=100)
parent_name = models.CharField(max_length=100)
NIN_number = models.CharField(max_length=20, null=True, blank=True, default='0')
period_of_stay = models.CharField(max_length=50,null=True, blank=True, default='Full Day')
amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
 baby_number = models.CharField(max_length=20)
registered_on = models.DateField(default=timezone.now)
sitter = models.ForeignKey('Sitter', on_delete=models.SET_NULL, null=True, related_name='babies')

    def __str__(self):
        return self.name

#Sitter model
class Sitter(models.Model):
name = models.CharField(help_text='Write the both first and last name of the sitter', max_length=100)
location = models.CharField(max_length=100)
date_of_birth = models.DateField(('birth date'), default=date.today)
gender = models.CharField(max_length=10)  
 religion = models.CharField(max_length=50, blank=True)
education_level = models.CharField(max_length=100)
sitter_number = models.CharField(max_length=20)
contact = models.CharField(max_length=15)
def **str**(self):
return self.name

#Product model
class Product(models.Model):
baby = models.ForeignKey('Baby', on_delete=models.CASCADE)
amount = models.DecimalField(max_digits=10, default='0', decimal_places=2)  
 Product_type = models.CharField(max_length=50,default='0')
Product_date = models.DateField(auto_now_add=True)
date = models.DateField(default=timezone.now)  
 def **str**(self):
return f'{self.baby.name} - {self.amount} UGX on {self.date}'

#Procurement model
class Procurement(models.Model):
item_name = models.CharField(max_length=100)
quantity = models.IntegerField()
price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
purchase_date = models.DateField()

    def __str__(self):
        return f'{self.item_name} - {self.quantity} units at {self.price_per_unit} UGX each'

#Sale model
class Sale (models.Model):
baby = models.ForeignKey('Baby', on_delete=models.CASCADE)
amount = models.DecimalField(max_digits=10, decimal_places=2)
sale_type = models.CharField(max_length=50)
date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.baby.name} - {self.amount} UGX on {self.date}'

class Transaction(models.Model):
amount = models.DecimalField(max_digits=10, decimal_places=2)
transaction_type = models.CharField(max_length=50)
date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} UGX on {self.date}'

#Report(models.Model)
class Report(models.Model):
report_type = models.CharField(max_length=100)
created_at = models.DateTimeField(auto_now_add=True)
file_path = models.FileField(upload_to='reports/')

    def __str__(self):
        return f'{self.report_type} - {self.created_at}'

# class Registration(models.Model):

# email = models.EmailField(max_length=254)

# password = models.CharField(max_length=100)

# confirm_password = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.email

................................
