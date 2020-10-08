from django import forms
from .models import members, dailyTransactions, productadding, expensesM, stafflist
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class Login(forms.Form):
    username = forms.CharField(label="Username",  max_length=200)
    password = forms.CharField(max_length=200, label="Password", widget=forms.PasswordInput)
    
    
class Stafflister(forms.ModelForm):
    staffname = forms.CharField(label = '', max_length=200, widget = forms.TextInput(attrs={'placeholder':'Staffname'}))
    staffemail = forms.EmailField(label = '', widget = forms.EmailInput(attrs={'placeholder':'Staff Email'}))
    staffnumber = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'Staff Number'}))
    staffpassword = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder':'Staff Password'}))
    class Meta:
        model = stafflist
        fields = ('staffname', 'staffemail','staffnumber', 'staffpassword')

    
class memberForm(forms.ModelForm):
    class Meta:
        model = members
        fields = ('name','cust_type','gender','date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'})
        }
   
class Transform(forms.ModelForm):
    class Meta: 
        model = dailyTransactions
        fields = ('service_name','customer_name','service_rate','Paid_amount','return_amount', 'staffName', 'total_amount')
        widgets = {
            'service_rate': forms.TextInput(attrs={'id':'service'}),
            'Paid_amount': forms.TextInput(attrs={'id':'paid'}),
            'return_amount': forms.TextInput(attrs={'id':'return'}),
            'total_amount': forms.TextInput(attrs={'id':'total'})
        }

class productAdd(forms.ModelForm):
    class Meta:
        model = productadding
        fields = ('product_name', 'product_price', 'product_Image')

class dateforHistory(forms.Form):
    date = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date'}))

class expensesform(forms.ModelForm):
    class Meta:
        model = expensesM
        fields = ('expenses', 'rate')