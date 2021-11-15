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
    path('add-category', views.add_category_view, name='add-category'),
    path('update-category/<int:pk>', views.update_category_view, name='update-category'),
    path('delete-category/<int:pk>',views.delete_category_view, name='delete-category'),

    path('order-dashboard', views.order_dashboard_side_var_view, name='order-dashboard'),
    path('total-order-list', views.total_order_list_view, name='total-order-list'),
    path('order-view/<int:pk>', views.single_order_view, name='order-view'),
    path('pending-order-list', views.pending_order_list_view, name='pending-order-list'),
    path('processing-order-list', views.processing_order_list_view, name='processing-order-list'),
    path('shipped-order-list', views.shipped_order_list_view, name='shipped-order-list'),
    path('delivered-order-list', views.delivered_order_list_view, name='delivered-order-list'),

]