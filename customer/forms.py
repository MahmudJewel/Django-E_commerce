from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from flatpickr import DatePickerInput

from django.contrib.auth.models import User
from .models import Customer

# first time register form
class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


 # ********** start Change profile form ***************
class EditForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

class customerForm(forms.ModelForm):
    #birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
    #birth_date = forms.DateField(widget=DatePickerInput())
    class Meta:
        model = Customer
        fields = ["birth_date", "profile_pic", "address", "mobile"]

# ********** end Change profile form ***************


# ********** start shipping address ***************
# class shippingUserPart1(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name"]

# class shippingUserPart2(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ["mobile", "address"]

# ********** end shipping address ***************
