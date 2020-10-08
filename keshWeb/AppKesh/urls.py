from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/member', views.dashboard, name='member'),
    path('deletemember/<int:mem_id>', views.deletemember, name="deletemember"),
    path('dashboard/transaction', views.transaction, name="transaction"),
    path('dashboard/history', views.history, name="history"),
    path('dashboard/branch', views.branch, name="branch"),
    path('pricing/', views.price, name="price"),
    path('products/', views.product, name="product"),
    path('dashboard/addproducts/', views.addproduct, name="addproduct"),
    path('dashboard/AdditionalTransaction/', views.addT, name="addT"),
    path('dashboard/StaffTransactions', views.staffT, name='staffT'),
    path('StaffAcc', views.staff, name="staff"),
    path('addstaff', views.addstaff, name = "addstaff"),
]