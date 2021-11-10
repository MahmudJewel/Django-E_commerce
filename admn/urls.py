from django.contrib import admin
from django.urls import path, include

from admn import views

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('admin-customer', views.admin_customer_side_var, name='admin-customer'),
    path('update-customer/<int:pk>', views.update_customer_view, name='update-customer'),
    path('delete-customer/<int:pk>',views.delete_customer_view, name='delete-customer'),
    path('customer-list', views.customer_list_view, name='customer-list'),

    path('admin-product', views.admin_product_side_var, name="admin-product"),
    path('add-product', views.add_product_view, name="add-product"),
    path('product-list', views.product_list_view, name='product-list'),
    path('update-product/<int:pk>', views.update_product_view, name='update-product'),
    path('delete-product/<int:pk>',views.delete_product_view, name='delete-product'),

    path('product-category', views.category_side_var_view, name='product-category'),
    path('category-list', views.category_list_view, name='category-list'),

]