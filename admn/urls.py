from django.contrib import admin
from django.urls import path, include

from admn import views

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('admin-customer', views.admin_customer_side_var, name='admin_customer_side_var'),
    
    
]