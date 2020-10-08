from django.db import models
from datetime import date
# Create your models here.
class members(models.Model):
    name = models.CharField(max_length=200)
    cust_type = models.CharField(max_length=200, choices=(
        ('Regular','Regular'),
        ('Irregular', 'Irregular')
    ))
    gender = models.CharField(max_length=200, choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ))
    date_of_birth = models.DateField()
    date_added = models.DateField(auto_now_add=True)
dailyTransactions = "RecordFor"+str(date.today())



class stafflist(models.Model):
    staffname = models.CharField(max_length = 200)
    staffemail = models.EmailField(max_length = 200)
    staffnumber = models.CharField(max_length = 200)
    staffpassword = models.CharField(max_length= 200)
class dailyTransactions(models.Model):
    service_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    service_rate = models.IntegerField()
    staffName = models.CharField(max_length=200, choices=(
        ('Staff-1', 'One'),
        ('Staff-2', 'Two'),
        ('Staff-3', 'Three'),
        ('Owner', 'Owner')
    ))
    Paid_amount = models.IntegerField()
    return_amount = models.IntegerField()
    total_amount = models.IntegerField()
    date_of_transaction = models.DateField(auto_now_add=True)

class productadding(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    product_Image = models.ImageField(upload_to="productImage/%Y/%m/%d", blank=True)

class expensesM(models.Model):
    expenses = models.CharField(max_length=200)
    rate = models.IntegerField()
    date_of_expenses = models.DateField(auto_now_add=True)
    
