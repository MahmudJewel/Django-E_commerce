from django.contrib import admin
from django.urls import path, include
from customer import views

urlpatterns = [
    path('signup',views.customerSignup, name='signup'),
    path('profile/<int:pk>', views.upadate_profile_view, name='profile'),
]