from django.contrib import admin
from django.urls import path, include

from admn import views

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('admin-customer', views.admin_customer_side_var, name='admin-customer'),
    path('update-customer/<int:pk>', views.update_customer_view, name='update-customer'),
    path('delete-customer/<int:pk>',views.delete_customer_view, name='delete-customer'),
    
]