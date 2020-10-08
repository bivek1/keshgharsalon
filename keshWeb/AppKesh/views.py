from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib import messages
from .forms import memberForm, Transform, productAdd, dateforHistory, expensesform, Stafflister
from .models import members, dailyTransactions, productadding, expensesM, stafflist
from datetime import date
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
# Create your views here.
def home(request):
    current_user = request.user
    productData = productadding.objects.all()
    fivedata = []
    a = 0
    for i in productData:
        fivedata.append(i)
        a = a+1
        if a == 6:
            break
    # aa =0
    dat = {
        'data':fivedata,
    }
    return render(request, "index.html", dat)
@login_required
def dashboard(request):
    current_user = request.user
    if current_user.is_staff == True:    
        us = request.user
        mem = memberForm(request.POST or None)
        memData = members.objects.all()
        paginator = Paginator(memData, 6)
        page = request.GET.get('page')
        print(page)
        try:
            aa = int(page)
        except:
            aa = 1
        print(type(aa))
        print(type(page))
        memData = paginator.page(aa)
        data = {
            'memberform':mem,
            'memData': memData,
            'ti': date.today(),
            'da': members.objects.order_by('date_of_birth')
        }
        if mem.is_valid():
            mem.save()
            messages.success(request, 'Member added sucessfully')
            return HttpResponseRedirect('/dashboard/member')
        
        return render(request, 'member.html', data)
    else:
        return HttpResponse("<h1>Sorry You are not eligible to view or edit this page</h1>")

@login_required
def deletemember(request, mem_id):
    member_delete = members.objects.get(id = mem_id)
    member_delete.delete()
    messages.success(request, 'Member Deleted sucessfully')
    return HttpResponseRedirect('/dashboard/member')
def product(request):
    current_user = request.user
    if current_user.is_staff == True:  
        productData = productadding.objects.all()

        data = {
            'data':productData
        }

        return render(request, "products.html", data)
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
    
def price(request):
    return render(request, "pricingtraining.html")

@login_required
def addproduct(request):
    current_user = request.user
    if current_user.is_staff == True: 
        us = request.user
        if request.method == 'POST':
            form = productAdd(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Your product has been added")
                return HttpResponseRedirect("/dashboard/addproducts")
        else:
            prodform = productAdd()
            dic = {
            'proform': prodform
            }
        
            return render(request, "addproduct.html", dic)
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
    
@login_required
def transaction(request):
    form = Transform()
    formTrans = Transform(request.POST or None)
    Transaction = dailyTransactions.objects.all()
    expensesF = expensesform(request.POST or None)
    # expensesM = expensesM()
    dict = {
        'formT': formTrans,
        'trans': Transaction,
        'exp'  : expensesF
    }
    if formTrans.is_valid():
        formTrans.save()
        messages.success(request, 'Income added sucessfully')
        return HttpResponseRedirect('/dashboard/transaction')
    elif expensesF.is_valid():
        expensesF.save()
        messages.success(request, 'Expenses added sucessfully')
        return HttpResponseRedirect('/dashboard/transaction')
    else:
        return render(request, 'transaction.html', dict)


@login_required
def expenses(request):
    expensesF = expensesform(request.POST or None)
    dict = {
        'exp'  : expensesF
    }
    if  expensesF.is_valid():
        expensesF.save()
        messages.success(request, 'Transaction added sucessfully')
        return HttpResponseRedirect('/dashboard/transaction')
    else:
        return render(request, 'transaction.html', dict)
@login_required
def history(request):
    current_user = request.user
    if current_user.is_staff == True: 
        us = request.user
        datefield = dateforHistory()
        dateTody = date.today()
        stringdate = str(dateTody)
        aa = stringdate.replace("-",",")
        aadate = aa.split(",")
        aaYear = int(aadate[0])
        aaMonth = int(aadate[1])
        aaDay = int(aadate[2])
        Transaction = dailyTransactions.objects.filter(date_of_transaction__contains=date(aaYear,aaMonth,aaDay))
        expenses = expensesM.objects.filter(date_of_expenses__contains=date(aaYear,aaMonth,aaDay))
        totalexpenses = expensesM.objects.filter(date_of_expenses__contains=date(aaYear,aaMonth,aaDay)).aggregate(total=Sum('rate'))
        total = dailyTransactions.objects.filter(date_of_transaction__contains=date(aaYear,aaMonth,aaDay)).aggregate(total=Sum('total_amount'))
        print(totalexpenses['total'])
        p1 = 0
        p2 = 0
        if total['total']:
            p1 = total['total']
        if totalexpenses['total']:
            p2 = totalexpenses['total']
    
        dict = {
            'trans': Transaction,
            'sum':total,
            'exp':expenses,
            'expt':totalexpenses,
            'datefield': datefield,
            'profit': p1-p2
        }
        if request.method == 'POST':
            try:
                if datefield.is_valid:
                    DateChoosen = request.POST['date']
                    DateChoosenStr = str(DateChoosen)
                    aa = DateChoosenStr.replace("-",",")
                    print(aa)
                    aadate = aa.split(",")
                    aaYear = int(aadate[0])
                    aaMonth = int(aadate[1])
                    aaDay = int(aadate[2])
                    Transaction = dailyTransactions.objects.filter(date_of_transaction__contains=date(aaYear,aaMonth,aaDay))
                    expenses = expensesM.objects.filter(date_of_expenses__contains=date(aaYear,aaMonth,aaDay))
                    totalexpenses = expensesM.objects.filter(date_of_expenses__contains=date(aaYear,aaMonth,aaDay)).aggregate(total=Sum('rate'))
                    total = dailyTransactions.objects.filter(date_of_transaction__contains=date(aaYear,aaMonth,aaDay)).aggregate(total=Sum('total_amount'))
                    p1 = 0
                    p2 = 0
                    if total['total']:
                        p1 = total['total']
                    if totalexpenses['total']:
                        p2 = totalexpenses['total']
                    dicted = {
                    'totaltra': total,
                    'hisdata':Transaction,
                    'dayexpenses': totalexpenses,
                    'hisex': expenses,
                    'date':DateChoosen,
                    'datefield': datefield,
                    'profits':p1-p2
                    }
                    return render(request, 'history.html', dicted)    
                else:
                    return render(request, 'history.html', dict)
            except:
                dic = {
                    'datefield': datefield,
                }
                messages.error(request,"Please enter date as in Input Box")
                return render(request, 'history.html', dic)
        else:
            return render(request, 'history.html', dict)
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
    
@login_required
def branch(request):
    grp = Group.objects.filter(name = 'staff')
    print(grp)
    return render(request, 'branch.html')

@login_required
def addT(request):
    current_user = request.user
    if current_user.is_staff == True:
        if request.method == 'POST':
            dateBegin = request.POST['dateforbegin']
            dateEnd = request.POST['dateforend']
            Db = str(dateBegin)
            dE = str(dateEnd)
            trans = dailyTransactions.objects.filter(date_of_transaction__gte=Db, date_of_transaction__lte=dE)
            expenses = expensesM.objects.filter(date_of_expenses__gte=Db, date_of_expenses__lte=dE) 
            totalexpenses = expensesM.objects.filter(date_of_expenses__gte=Db, date_of_expenses__lte=dE).aggregate(total=Sum('rate'))
            total = dailyTransactions.objects.filter(date_of_transaction__gte=Db, date_of_transaction__lte=dE).aggregate(total=Sum('total_amount'))
            p1 = 0
            p2 = 0
            if total['total']:
                p1 = total['total']
            if totalexpenses['total']:
                p2 = totalexpenses['total']
            datadic = {
                'totaltra': total,
                'dayexpenses': totalexpenses,
                'trans': trans,
                'expenses': expenses,
                'profits':p1-p2,
                'DB': dateBegin,
                'DE': dateEnd,
                'message': "SORRY WE DO NOT FIND ANY TRANSACTION"
            }
            return render(request, "addT.html", datadic)
        else:
            return render(request, "addT.html")
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
@login_required
def staffT(request):
    current_user = request.user
    if current_user.is_staff == True:
        if request.method == 'POST':
            staffname = request.POST['staff']
            dateBegin = request.POST['dateforbegin']
            dateEnd = request.POST['dateforend']
            Db = str(dateBegin)
            dE = str(dateEnd)
            trans = dailyTransactions.objects.filter(staffName= staffname ,date_of_transaction__gte=Db, date_of_transaction__lte=dE)
            total = dailyTransactions.objects.filter(staffName= staffname ,date_of_transaction__gte=Db, date_of_transaction__lte=dE).aggregate(total=Sum('total_amount'))
            p1 = 0
            if total['total']:
                p1 = total['total']
            dict = {
                'totaltra': total,
                'trans': trans,
                'profits':p1,
                'DB': dateBegin,
                'DE': dateEnd,
                'staff': staffname,
                'message': "SORRY WE DO NOT FIND ANY TRANSACTION"
            }
            return render(request, "staffT.html", dict)
        else:
            return render(request, "staffT.html")
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
    

@login_required
def staff(request):
    return render(request, 'user.html')

@login_required
def addstaff(request):
    current_user = request.user
    if current_user.is_staff == True:
        staffform = Stafflister(request.POST or None)
        dist ={
            'staffform': staffform ,
        }
        if staffform.is_valid():
            cd = staffform.cleaned_data
            user = User.objects.create_user(cd['staffname'], cd['staffemail'], cd['staffpassword'])
            staffform.save()
            my_group = Group.objects.get(name = 'staff')
            id = user.id
            my_group.user_set.add(id)
            messages.success(request, 'New Staff Added Sucessfully!')
            return HttpResponseRedirect('addstaff')
        else:
            return render(request, 'addstaff.html', dist)
    else:
        return HttpResponse("<h1>Sorry you are not eligible to view or edit this page</h1>")
