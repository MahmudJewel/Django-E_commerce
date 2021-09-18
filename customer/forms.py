from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from flatpickr import DatePickerInput

from django.contrib.auth.models import User
from .models import Customer

class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


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