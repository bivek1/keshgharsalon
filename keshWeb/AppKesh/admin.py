from django.contrib import admin
from .models import members, dailyTransactions, productadding, expensesM, stafflist
# Register your models here.
admin.site.register(members)
admin.site.register(dailyTransactions)
admin.site.register(productadding)
admin.site.register(expensesM)
admin.site.register(stafflist)