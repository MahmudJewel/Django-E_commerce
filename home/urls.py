from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

from home import views


urlpatterns = [
    path('',views.home),
    path('login', LoginView.as_view(template_name='home/login.html'), name='login'),


]