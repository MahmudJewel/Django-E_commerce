from django.contrib import admin
from django.urls import path, include

from admn import views

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    
]