from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from customer import forms as CFORM
from customer import models as CMODEL

# Create your views here.
def customerSignup(request):
	userForm = CFORM.UserForm()
	customerForm = CFORM.CustomerForm()
	if request.method == 'POST':
		userForm=CFORM.UserForm(request.POST)
		customerForm = CFORM.CustomerForm(request.POST, request.FILES)
		#print(userForm.first_name)
		if userForm.is_valid() and customerForm.is_valid() :
			user=userForm.save()
			user.set_password(user.password)
			user.save()
			customer= customerForm.save(commit=False)
			customer.user=user
			customer.save()
			customer_group=Group.objects.get_or_create(name='CUSTOMER')
			customer_group[0].user_set.add(user)
		return redirect('login')
			
	context={
		'customerForm': customerForm,
		'userForm' : userForm
	}
	return render(request, 'customer/signup.html',context)

