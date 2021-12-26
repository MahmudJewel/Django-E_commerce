from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from home import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('home/', views.customer_home, name='customer_home'),

    path('login', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    path('product/<int:pk>',  views.product_view, name='product'),
    path('cart', views.cart_view, name='cart'),
    path('checkout', views.checkout_view, name='checkout'),
    path('search', views.search_view, name='search')
]